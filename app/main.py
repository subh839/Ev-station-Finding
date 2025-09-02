# app/main.py
from fastapi import FastAPI
from .database import engine, Base
from .routes import auth_routes, station_routes, predict_routes

# create DB tables
from . import models
Base.metadata.create_all(bind=engine)

app = FastAPI(title="EV Charging Backend")

app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(station_routes.router, prefix="/stations", tags=["stations"])
app.include_router(predict_routes.router, prefix="/predict", tags=["predict"])
