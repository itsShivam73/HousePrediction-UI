import streamlit as st
import requests

API_URL = "https://house-prediction-0h9n.onrender.com/predict"

st.title("🏠 House Price Prediction App")

st.markdown(
    "Enter the details of the house below and click **Predict** to get the estimated price."
)

# Take input from user
longitude = st.text_input("Longitude (optional, e.g., -121.8)")
latitude = st.text_input("Latitude (optional, e.g., 37.32)")
housing_median_age = st.number_input("Housing Age", min_value=1, max_value=100, value=14)
total_rooms = st.number_input("Total Rooms", min_value=1, value=4412)
total_bedrooms = st.number_input("Total Bedrooms", min_value=1, value=924)
population = st.number_input("Population", min_value=1, value=2698)
households = st.number_input("Households", min_value=1, value=891)
median_income = st.number_input("Median Income", min_value=0.0, value=4.7027, format="%.2f")
ocean_proximity = st.selectbox("Ocean Proximity", ["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY"])

# Button to predict
if st.button("Predict"):
    # Convert text input to float, handle empty input
    try:
        longitude_val = float(longitude) if longitude else -121.8
        latitude_val = float(latitude) if latitude else 37.32
    except ValueError:
        st.error("Longitude and Latitude must be numbers!")
        st.stop()

    # Prepare payload
    payload = {
        "longitude": longitude_val,
        "latitude": latitude_val,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }

    # Call API
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        prediction = response.json()["prediction"]
        st.success(f"🏠 Predicted House Value: ${prediction:,.2f}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error calling API: {e}")