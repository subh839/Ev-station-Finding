# app/routes/station_routes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..deps import get_db, get_current_user
from math import radians, sin, cos, asin, sqrt

router = APIRouter()

def haversine(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1; dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return 6371 * c

@router.get("/nearby", response_model=List[schemas.StationOut])
def nearby(lat: float, lon: float, radius_km: float = 5.0, min_power_kw: float = 0.0,
           db: Session = Depends(get_db), user = Depends(get_current_user)):
    stations = db.query(models.Station).all()
    out = []
    for s in stations:
        if s.lat is None or s.lon is None: continue
        d = haversine(lat, lon, s.lat, s.lon)
        if d <= radius_km and (s.power_class_kw or 0.0) >= min_power_kw:
            out.append(s)
    # SQLAlchemy model objects can be returned because Pydantic orm_mode
    # We can sort them by distance (optional)
    # For simplicity, just return first N sorted by distance:
    out_sorted = sorted(out, key=lambda s: haversine(lat, lon, s.lat, s.lon))
    return out_sorted[:50]
