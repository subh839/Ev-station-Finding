# app/ml_wrapper.py
import os
import joblib
import numpy as np

# Path to trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "ml_models/ev_first_year_model.pkl")

# Load model once
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None
    print(f"⚠️ Model not found at {MODEL_PATH}. Train the model first.")

def predict_range(battery_kwh: float, efficiency_wh_per_km: float,
                  start_soc: float = 100.0, target_soc: float = 20.0,
                  power_class_kw: float = 50.0) -> float:
    """
    Predict EV range based on battery, efficiency, SOC, and power class.
    Uses the trained LinearRegression model.
    """
    if model is None:
        raise ValueError("Model not loaded. Train it first.")

    # Prepare input for model prediction
    X = np.array([[battery_kwh, efficiency_wh_per_km]])
    base_range = model.predict(X)[0]

    # Scale range according to SOC difference
    soc_fraction = (start_soc - target_soc) / 100.0
    predicted_range = base_range * soc_fraction

    # Adjust for power_class_kw (simple example)
    predicted_range *= min(1.0, power_class_kw / 100.0)

    return predicted_range
