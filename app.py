import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("dynamic_pricing_model.pkl")

st.title("AI Dynamic Pricing Engine")

# Inputs
inventory = st.slider("Inventory Level",0,500)
demand = st.slider("Demand Forecast",0,500)
competitor = st.slider("Competitor Pricing",0,200)

# Prediction
if st.button("Predict Price"):

    input_data = np.array([[inventory, demand, competitor]])

    price = model.predict(input_data)

    st.subheader("Recommended Price")
    st.metric("Optimal Price", round(price[0],2))
    st.success(f"Recommended Price: {price[0]:.2f}")
