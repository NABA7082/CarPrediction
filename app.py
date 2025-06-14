import streamlit as st
import pickle
import numpy as np

# Load the model
with open('carPrediction.pkl', 'rb') as file:
    regressor = pickle.load(file)

st.title("Car Price Prediction App")

# User Inputs
year = st.number_input("Year of Purchase", min_value=1990, max_value=2025, step=1)
present_price = st.number_input("Present Price (in Lakhs)", step=0.1)
kms_driven = st.number_input("KMs Driven", step=100)
owner = st.selectbox("Number of Previous Owners", [0, 1, 2, 3])
fuel_type = st.selectbox("Fuel Type", ['Petrol', 'Diesel','CNG'])
seller_type = st.selectbox("Seller Type", ['Dealer', 'Individual'])
transmission = st.selectbox("Transmission Type", ['Manual', 'Automatic'])

# Encoding

fule_encoded={"Petrol":0,"Diesel":1,"CNG":2}[fuel_type]
seller_individual = 1 if seller_type == 'Individual' else 0
trans_manual = 1 if transmission == 'Manual' else 0


# Convert present price to rupees if model expects it in rupees
present_price_rupees = present_price * 100000

if st.button("Predict Price"):
    input_data = np.array([[year,present_price_rupees, kms_driven, owner, fule_encoded, seller_individual, trans_manual]])
    prediction = regressor.predict(input_data)

    # Convert predicted price to Lakhs for display (if prediction is in rupees)
    predicted_price_lakhs = prediction[0] / 100000

    st.success(f"Estimated Selling Price: ₹ {round(predicted_price_lakhs, 2)} Lakhs")

