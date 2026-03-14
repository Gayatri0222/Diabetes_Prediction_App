
# 🌟 **Diabetes Prediction App (Streamlit + Logistic Regression)**

A simple and user-friendly web application built with **Machine Learning** and **Streamlit** to predict whether a person is likely to have diabetes based on key medical features.

---

## 🚀 **Live Demo**

👉 *Add your Streamlit Cloud link here once deployed:*

```

```

---

## 📌 **Project Overview**

This project uses the **PIMA Indians Diabetes Dataset** to build a **Logistic Regression** model that predicts diabetes outcome (0 = No Diabetes, 1 = Diabetes).
The trained model is deployed using **Streamlit**, allowing users to input medical information and receive predictions instantly.

---

## 📊 **Features Included**

* 🔍 Exploratory Data Analysis (EDA)
* 🧹 Data preprocessing
* 🧠 Machine Learning model (Logistic Regression)
* 💾 Model saved using **joblib**
* 🌐 Web app created using **Streamlit**
* 🎨 Interactive input sliders & clean UI
* 🚀 Deployed using Streamlit Community Cloud

---

## 🧠 **Model Inputs**

The app takes the following user inputs:

| Feature                    | Description                  |
| -------------------------- | ---------------------------- |
| Pregnancies                | Number of pregnancies        |
| Glucose                    | Plasma glucose concentration |
| Blood Pressure             | Diastolic blood pressure     |
| Skin Thickness             | Triceps skin fold thickness  |
| Insulin                    | 2-Hour serum insulin         |
| BMI                        | Body mass index              |
| Diabetes Pedigree Function | Diabetes hereditary score    |
| Age                        | Age of the patient           |

---

## 🏗 **Tech Stack**

### **Machine Learning**

* Logistic Regression
* scikit-learn
* pandas
* numpy

### **Deployment**

* Streamlit
* Streamlit Cloud
* GitHub

---

## 📁 **Project Structure**

```
diabetes-streamlit-app/
│── app.py
│── logistic_regression_model.pkl
│── requirements.txt
│── README.md
```

---

## ⚙️ **How to Run Locally**

### 1️⃣ Install requirements

```
pip install -r requirements.txt
```

### 2️⃣ Run streamlit

```
streamlit run app.py
```

This will open the application in your browser at:
👉 [http://localhost:8501/](http://localhost:8501/)

---

## 🌐 **Deployment Instructions**

### ✔ Upload Project to GitHub

1. Create a new GitHub repo
2. Drag & drop:

   * `app.py`
   * `logistic_regression_model.pkl`
   * `requirements.txt`
   * `README.md`
3. Commit changes

### ✔ Deploy on Streamlit Cloud

1. Go to [https://share.streamlit.io](https://share.streamlit.io)
2. Log in with GitHub
3. Click **"New App"**
4. Select your repo
5. Choose:

   * Branch → `main`
   * App file → `app.py`
6. Click **Deploy**

In ~30 seconds, your public app link will be ready! 🎉

---

## 💡 **Future Enhancements**

* Add data visualization in the app
* Use multiple ML models (Random Forest, SVM, etc.)
* Improve UI with custom CSS
* Add patient report download option




* A **GIF demo**,
* Or a **better styled README with emojis + sections**.
