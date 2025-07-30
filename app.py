# app.py

import streamlit as st
import pandas as pd
import pickle

# Load model
with open('model.pkl', 'rb') as f:
    model, le = pickle.load(f)

st.set_page_config(page_title="Salary Predictor", page_icon="💰")

st.title("💼 Salary Prediction App")
st.write("Enter the details below to predict expected salary:")

# Input form
experience = st.slider("Years of Experience", 0, 20, 2)
education = st.selectbox("Education Level", ["Bachelor", "Master", "PhD"])
age = st.slider("Age", 18, 60, 25)

# Predict button
if st.button("Predict Salary"):
    edu_encoded = le.transform([education])[0]
    input_df = pd.DataFrame([[experience, edu_encoded, age]], columns=["experience", "education_level", "age"])
    prediction = model.predict(input_df)[0]
    
    st.success(f"💰 Estimated Salary: ₹{int(prediction):,}")
