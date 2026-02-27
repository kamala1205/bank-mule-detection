# 🛡️ Bank Mule Detection System

A Machine Learning based web application that detects **Bank Mule Accounts** using transaction behavior analysis.  
The system classifies accounts as **Mule**, **Suspicious**, or **Legitimate** in real-time.

This project is developed as part of the **MCA Final Year Project**.

---

## 🚀 Live Demo

🔗 Live App:
https://kamala1205-bank-mule-detection-streamlit-app.streamlit.app

🔗 Portfolio:
https://kamala1205.github.io

🔗 Dashboard:
https://kamala1205.github.io/bank-mule-detection/dashboard_bank_mule.html

---

## 📌 Project Features

✔ Machine Learning Model (Random Forest)  
✔ Real-time Fraud Detection  
✔ Risk Score Prediction  
✔ Feature Contribution Visualization  
✔ SQLite Database Logging  
✔ Interactive Streamlit Interface  
✔ Dashboard Analytics  
✔ Professional UI Design

---

## 🧠 Machine Learning Model

Algorithm Used:

- Random Forest Classifier

Accuracy:

- **96.4% Accuracy**

Input Features:

- Account Age
- Phone Number Changes
- Transaction Count
- Transaction Amount
- Pass-through Ratio

Output:

- Mule Account 🚨
- Suspicious Account ⚠️
- Legitimate Account ✅

---

## 🛠️ Technologies Used

### Programming

- Python
- Machine Learning

### Libraries

- Streamlit
- Scikit-learn
- NumPy
- Pandas

### Database

- SQLite

### Frontend

- HTML
- CSS

---

## 📂 Project Structure
bank-mule-detection/
│
├── streamlit_app.py
├── model.pkl
├── bank.db
├── requirements.txt
└── README.md


streamlit run streamlit_app.py


---

## 📊 How It Works

1. User enters account details
2. Machine Learning model analyzes behavior
3. Risk score is calculated
4. Account classified as:

- Mule
- Suspicious
- Legitimate

5. Data stored in SQLite database

---

## 📈 Risk Score Levels

| Risk Score | Classification |
|----------|----------------|
| 0 – 35% | Legitimate |
| 35 – 60% | Suspicious |
| 60 – 100% | Mule |

---

## 💾 Database

All predictions are stored in:


bank.db


Stored Data:

- Account Age
- Phone Changes
- Transaction Count
- Transaction Amount
- Pass-through Ratio
- Prediction
- Risk Score
- Date

---

## 🎯 Project Objective

The objective of this project is to detect **Money Mule Accounts** in banking systems using **Machine Learning techniques**.

This helps banks:

- Prevent fraud
- Detect suspicious accounts
- Reduce financial crime

---

## 👨‍💻 Author

**Kamalakanta Behera**

MCA Final Year Student  
Data Analyst | Machine Learning Enthusiast

Portfolio:
https://kamala1205.github.io

GitHub:
https://github.com/kamala1205

---

## ⭐ Future Improvements

- Deep Learning Model
- Real Banking Dataset
- API Integration
- Live Transaction Monitoring
- Advanced Dashboard

---

## 📜 License

This project is for **educational purposes only**.
