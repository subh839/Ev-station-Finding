import os
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data/ev_models_2025.csv")

# Encode categorical features
categorical_cols = ['powertrain', 'body_style', 'origin_country', 'market_regions']
df_encoded = pd.get_dummies(df, columns=categorical_cols)

# Features & target
X = df_encoded.drop(columns=['first_year', 'make', 'model'])  # drop target & identifiers
y = df_encoded['first_year']

# Train model
model = LinearRegression()
model.fit(X, y)

# Ensure directory exists
model_dir = "app/ml_models"
os.makedirs(model_dir, exist_ok=True)

# Save model
model_path = os.path.join(model_dir, "ev_first_year_model.pkl")
joblib.dump(model, model_path)

print(f"✅ Model trained & saved at '{model_path}'")
print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)