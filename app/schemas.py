# app/schemas.py
from pydantic import BaseModel
from typing import Optional

# auth
class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# station
class StationIn(BaseModel):
    station_id: Optional[str]
    name: str
    lat: float
    lon: float
    address: Optional[str] = ""
    power_class_kw: Optional[float] = None

class StationOut(StationIn):
    id: int
    class Config:
        orm_mode = True

# predict
class PredictIn(BaseModel):
    model_id: Optional[str] = None
    battery_kwh: Optional[float] = None
    efficiency_wh_per_km: Optional[float] = None
    start_soc: float = 0.2
    target_soc: float = 0.8
    station_id: Optional[str] = None
    power_class_kw: Optional[float] = None
