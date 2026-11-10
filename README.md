# Consumer Loan Approval Prediction System

A Machine Learning-based web application that predicts the likelihood of consumer loan approval based on customers' personal, financial, and banking information.

## 🌐 Live Demo

**Live Application:** https://consumer-loan-prediction-system.onrender.com

**GitHub Repository:** https://github.com/Durgabhavanithota/Consumer-Loan-Prediction-System

## 📌 Project Overview

The Consumer Loan Approval Prediction System is a team-based academic project developed by four members.

The application uses Machine Learning to analyze customer information and predict the likelihood of loan approval. Users can enter their personal, financial, and banking details through a user-friendly web interface and receive a prediction with a probability percentage.

## 🎯 Project Objectives

- Predict the likelihood of consumer loan approval.
- Analyze customer financial and banking information.
- Apply Machine Learning techniques to a real-world financial problem.
- Develop an interactive web application.
- Make the application accessible through online deployment.

## ✨ Key Features

- User-friendly loan application interface.
- Customer personal and financial information input.
- Machine Learning-based loan prediction.
- Prediction probability displayed as a percentage.
- Loan Approved and Loan Not Approved results.
- Responsive web interface.
- Live deployment using Render.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Backend | Flask |
| Frontend | HTML, CSS |
| Model Storage | Joblib |
| Deployment | Render |
| Version Control | Git, GitHub |

## 🤖 Machine Learning Model

The application uses a trained Random Forest classification model to predict loan approval.

The model considers the following 11 input features:

1. Age
2. Years of Experience
3. Family Size
4. Annual Income
5. Average Spending
6. Education Level
7. Mortgage
8. Securities Account
9. CD Account
10. Online Banking
11. Credit Card

The input data is transformed using a fitted scaler before prediction.

### Prediction Logic

The application uses a probability threshold of 0.30:

- Probability greater than or equal to 30%: Loan Approved.
- Probability below 30%: Loan Not Approved.

*Note: This threshold is configured for this academic project and does not represent an actual bank's lending policy.*

## 📂 Project Structure

Consumer-Loan-Prediction-System/
│
├── templates/
│   ├── loan_app.html
│   └── result.html
│
├── app.py
├── loan_model.pkl
├── scaler.pkl
├── train_model.ipynb
├── requirements.txt
├── .gitignore
└── README.md


## ⚙️ Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the repository

git clone https://github.com/Durgabhavanithota/Consumer-Loan-Prediction-System.git

### 2. Navigate to the project folder

cd Consumer-Loan-Prediction-System

### 3. Install dependencies

pip install -r requirements.txt

### 4. Run the application

python app.py

### 5. Open in your browser

http://127.0.0.1:5000


## 🚀 Deployment

The application is deployed using Render and connected to GitHub.

**Live Application:** https://consumer-loan-prediction-system.onrender.com

## 👥 Team Project

**Project Type:** Team Project (4 Members)

This project was collaboratively developed by a team of four members, with responsibilities shared across frontend development, backend development, and Machine Learning.

### My Contributions

- Independently designed and developed the frontend user interface using HTML and CSS.
- Developed the Flask backend to connect the user interface with the Machine Learning model.
- Trained the Machine Learning model using the project dataset.
- Integrated the trained model into the application for loan prediction.
- Collaborated with team members during overall project development and deployment.

## 👩‍💻 Author

**B.Sc. Artificial Intelligence Student**

GitHub: https://github.com/Durgabhavanithota

## 📄 Disclaimer

This project is developed for academic and educational purposes. Its predictions are based on a trained Machine Learning model and should not be considered actual financial or loan approval decisions.