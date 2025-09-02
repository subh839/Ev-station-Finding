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


[Client - React TS]  <----HTTPS---->  [Load Balancer/Ingress]
                                         |
                                 [Backend - FastAPI (Docker)]
                                         |
        +------------------------+-------+------------------------+
        |                        |                                |
   [Postgres DB]         [Model Artifact Storage (S3)]         [LLM Service]
        |                         (or local volume)             (OpenAI / HF API)
        |
   [Monitoring / Logs]
