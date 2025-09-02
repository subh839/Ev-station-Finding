# app/routes/auth_routes.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, schemas, auth, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.Token)
def register(user_in: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.username == user_in.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed = auth.get_password_hash(user_in.password)
    user = models.User(username=user_in.username, hashed_password=hashed)
    db.add(user); db.commit(); db.refresh(user)
    token = auth.create_access_token(user.username)
    return {"access_token": token}

@router.post("/token", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    token = auth.create_access_token(user.username)
    return {"access_token": token}
