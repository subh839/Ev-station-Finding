import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# Load each dataset into DB
pd.read_csv("data/charging_stations_2025_world.csv").to_sql(
    "charging_stations", con=engine, if_exists="replace", index=False
)

pd.read_csv("data/ev_models_2025.csv").to_sql(
    "ev_models", con=engine, if_exists="replace", index=False
)

pd.read_csv("data/country_summary_2025.csv").to_sql(
    "country_summary", con=engine, if_exists="replace", index=False
)

pd.read_csv("data/world_summary_2025.csv").to_sql(
    "world_summary", con=engine, if_exists="replace", index=False
)

print("✅ All Excel data loaded into DB")
