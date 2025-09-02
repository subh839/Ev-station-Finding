# app/models.py
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(String, unique=True, index=True)
    name = Column(String)
    lat = Column(Float, index=True)
    lon = Column(Float, index=True)
    address = Column(Text)
    city = Column(String)
    country = Column(String)
    power_class_kw = Column(Float)
    connectors = Column(Text)

class EVModel(Base):
    __tablename__ = "ev_models"
    id = Column(Integer, primary_key=True, index=True)
    model_id = Column(String, unique=True, index=True)
    make = Column(String)
    model_name = Column(String)
    battery_kwh = Column(Float)
    rated_range_km = Column(Float)
    efficiency_wh_per_km = Column(Float)
