import streamlit as st
import joblib
import numpy as np
import pandas as pd

# 🔹 Load trained model
model = joblib.load("car_price_model.pkl")

st.title("🚗 Car Price Prediction App")
st.write("Enter car details below to predict the price")

# -------------------------
# 🔹 Numeric Inputs
# -------------------------
model_year = st.number_input("Model Year", 1990, 2025, 2020)
engine_size = st.number_input("Engine Size (Litres)", 0.5, 5.0, 2.0)
mileage = st.number_input("Mileage (km)", 0, 300000, 50000)
doors = st.number_input("Number of Doors", 2, 5, 4)
owner_count = st.number_input("Owner Count", 1, 5, 1)
horsepower = st.number_input("Horsepower", 50, 500, 150)

# -------------------------
# 🔹 Categorical Inputs
# -------------------------
brand = st.selectbox("Brand", ["Ford", "Honda", "Hyundai", "Tesla", "Toyota"])
fuel_type = st.selectbox("Fuel Type", ["Electric", "Hybrid", "Petrol"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# -------------------------
# 🔹 Predict Button
# -------------------------
if st.button("Predict Price 💰"):

    # Create dictionary with all columns = 0
    input_dict = {
        "Model_Year": model_year,
        "Engine_Size": engine_size,
        "Mileage": mileage,
        "Doors": doors,
        "Owner_Count": owner_count,
        "Horsepower": horsepower,
        "Brand_Ford": 0,
        "Brand_Honda": 0,
        "Brand_Hyundai": 0,
        "Brand_Tesla": 0,
        "Brand_Toyota": 0,
        "Fuel_Type_Electric": 0,
        "Fuel_Type_Hybrid": 0,
        "Fuel_Type_Petrol": 0,
        "Transmission_Manual": 0
    }

    # 🔹 Set selected brand to 1
    input_dict[f"Brand_{brand}"] = 1

    # 🔹 Set selected fuel type to 1
    input_dict[f"Fuel_Type_{fuel_type}"] = 1

    # 🔹 If Manual selected → 1, else 0
    if transmission == "Manual":
        input_dict["Transmission_Manual"] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Prediction
    prediction = model.predict(input_df)

    st.success(f"Estimated Car Price: ₹ {prediction[0]:,.2f}")