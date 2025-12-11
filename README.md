# Diabetes Prediction App

This project is a simple machine learning application that predicts whether a person has diabetes based on medical input features. The model is built using Logistic Regression and deployed using Streamlit.

---

## Project Overview

The project uses the PIMA Diabetes Dataset to train a Logistic Regression model. The trained model is saved using joblib and used inside a Streamlit web application for predictions.

Users can enter medical details such as glucose level, BMI, insulin, age, etc., and the app will predict whether the person is likely to have diabetes.

---

## Features

* Data loading and preprocessing
* Logistic Regression model training
* Model saved using joblib
* Streamlit-based web application
* User input fields for prediction
* Displays prediction result (Diabetic / Non-Diabetic)

---

## Input Features

The model uses the following features:

1. Pregnancies
2. Glucose
3. BloodPressure
4. SkinThickness
5. Insulin
6. BMI
7. DiabetesPedigreeFunction
8. Age

---

## Files in the Project

```
app.py
logistic_regression_model.pkl
requirements.txt
README.md
```

---

## How to Run the Project Locally

1. Install the required libraries:

```
pip install -r requirements.txt
```

2. Run the Streamlit app:

```
streamlit run app.py
```

3. The browser will open the app at:

```
http://localhost:8501
```

---

## Deployment Instructions (Streamlit Cloud)

1. Upload all project files to a GitHub repository
2. Go to: [https://share.streamlit.io](https://share.streamlit.io)
3. Log in with GitHub
4. Click "New App"
5. Select your repository
6. Choose the branch (main)
7. Select the file `app.py`
8. Click "Deploy"

Streamlit will generate a public link to your app.

---

## Requirements

Create a `requirements.txt` file with:

```
streamlit
scikit-learn
joblib
numpy
pandas
```


