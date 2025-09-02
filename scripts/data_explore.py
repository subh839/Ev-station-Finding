import pandas as pd

# Large dataset: charging stations
stations = pd.read_csv("data/charging_stations_2025_world.csv")
print("🔹 Charging Stations:", stations.shape)
print(stations.head(3))

# EV models dataset
ev_models = pd.read_csv("data/ev_models_2025.csv")
print("\n🔹 EV Models:", ev_models.shape)
print(ev_models.head(3))

# Country summary
country_summary = pd.read_csv("data/country_summary_2025.csv")
print("\n🔹 Country Summary:", country_summary.shape)
print(country_summary.head(3))

# World summary
world_summary = pd.read_csv("data/world_summary_2025.csv")
print("\n🔹 World Summary:", world_summary.shape)
print(world_summary.head(3))
