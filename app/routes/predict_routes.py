# app/routes/predict_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, models
from ..deps import get_db, get_current_user
from app.ml_wrapper import predict_range
router = APIRouter()

@router.post("/range")
def predict(payload: schemas.PredictIn, db: Session = Depends(get_db), user=Depends(get_current_user)):
    # if model_id given, fill battery & eff from DB
    battery = payload.battery_kwh
    eff = payload.efficiency_wh_per_km
    if payload.model_id:
        evrow = db.query(models.EVModel).filter(models.EVModel.model_id == payload.model_id).first()
        if not evrow:
            raise HTTPException(status_code=404, detail="EV model not found")
        if battery is None: battery = evrow.battery_kwh
        if eff is None: eff = evrow.efficiency_wh_per_km
    if battery is None or eff is None:
        raise HTTPException(status_code=400, detail="battery_kwh or efficiency_wh_per_km required (or supply model_id)")
    power = payload.power_class_kw or 50.0
    predicted = predict_range(float(battery), float(eff), float(payload.start_soc), float(payload.target_soc), float(power))
    return {"predicted_range_km": round(predicted, 2)}
