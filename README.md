ev_backend/
│── app/
│   ├── main.py                # Entry point
│   ├── models.py              # SQLAlchemy models
│   ├── schemas.py             # Pydantic schemas
│   ├── auth.py                # JWT Auth logic
│   ├── crud.py                # DB queries
│   ├── ml_model.py            # EV range prediction model
│   ├── routes/
│   │   ├── auth_routes.py     # Register/Login
│   │   ├── station_routes.py  # Charging station APIs
│   │   └── prediction_routes.py # AI endpoints
│── data/
│   └── ev_data.csv            # Your dataset
│── venv/                      # Virtual environment
│── requirements.txt


Backend: FastAPI

Database: SQLite / PostgreSQL (for simplicity we start with SQLite in development, can move to Postgres in prod)

AI Models:

Location Finder → Suggest nearest charging stations (Geospatial query).

Range Predictor → Predict how far EV can go after charging (ML regression model trained on dataset).

Security: JWT Authentication for users.
