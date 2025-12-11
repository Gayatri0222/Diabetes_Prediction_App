import streamlit as st
import numpy as np
import joblib

# Load model & scaler
model = joblib.load("logistic_regression_model.pkl")
scaler = joblib.load("scaler.pkl")   # REMOVE if not using scaler

st.title("Diabetes Prediction App")
st.write("Enter the patient details to predict the diabetes outcome.")

# Input fields
preg = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 300, 120)
bp = st.number_input("Blood Pressure", 0, 200, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 5.0, 0.5)
age = st.number_input("Age", 1, 120, 30)

if st.button("Predict"):
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

    # scale input (if model trained with scaler)
    input_data = scaler.transform(input_data)

    # prediction
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Patient is likely to have Diabetes.")
    else:
        st.success("Patient is unlikely to have Diabetes.")
