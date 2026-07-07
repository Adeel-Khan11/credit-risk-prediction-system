# Credit Risk Prediction System

An end-to-end machine learning application for predicting loan default probability, generating customer credit scores, and assessing credit risk through an interactive Streamlit dashboard.

**Live Application**

https://credit-risk-prediction-system-model.streamlit.app/

**GitHub Repository**

https://github.com/Adeel-Khan11/credit-risk-prediction-system

---

## Project Overview

Credit risk assessment is one of the most important processes in financial institutions. Traditional manual evaluation is often time-consuming and inconsistent, particularly when handling large volumes of loan applications.

This project presents an end-to-end credit risk prediction system developed to assist loan officers in evaluating applicants by predicting default probability, generating a credit score, assigning a customer risk category, and providing AI-assisted lending recommendations.

The application combines machine learning, explainable AI, interactive visualizations, and a modern web interface into a single deployable solution.

---

## Business Problem

The project is based on an industry-inspired business case where Lauki Finance, a Non-Banking Financial Company (NBFC), collaborates with AtliQ AI to build an automated credit risk assessment system.

The primary objectives are to:

- Predict the probability of loan default.
- Generate a customer credit score.
- Categorize applicants into different credit risk groups.
- Improve consistency in lending decisions.
- Reduce manual effort during loan approval.

---

## Features

### Machine Learning

- Credit default prediction
- Credit score generation
- Customer risk classification
- Bayesian hyperparameter optimization
- SHAP model explainability

### Streamlit Application

- Interactive dashboard
- Customer information form
- Loan details input
- Real-time prediction
- Plotly visualizations
- AI-based loan recommendation
- Downloadable PDF report

---

## Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn, XGBoost |
| Hyperparameter Optimization | Bayesian Optimization |
| Explainability | SHAP |
| Visualization | Plotly |
| Deployment | Streamlit |
| Model Serialization | Joblib |
| Report Generation | ReportLab |

---

## Project Structure

```text
credit-risk-prediction-system

│

├── app
│   ├── assets
│   │   └── style.css
│   ├── charts.py
│   ├── main.py
│   ├── prediction_helper.py
│   ├── recommendation.py
│   ├── report.py
│   └── utils.py
│
├── artifacts
│   └── model
│       └── model_data.joblib
│
├── credit_risk_model_fully_code.ipynb
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Machine Learning Workflow

1. Business Understanding
2. Data Collection
3. Data Cleaning
4. Exploratory Data Analysis
5. Feature Engineering
6. Data Encoding
7. Model Training
8. Hyperparameter Optimization
9. Model Explainability
10. Streamlit Deployment

---

## Model Development

Several classification algorithms were evaluated during model development, including:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

The final deployed model is an optimized XGBoost classifier tuned using Bayesian Optimization.

---

## Explainable AI

Model predictions are interpreted using SHAP (SHapley Additive Explanations), allowing users to understand how individual features contribute to prediction outcomes.

---

## Dashboard

The application provides:

- Customer Information
- Loan Details
- Credit Behaviour Analysis
- Default Probability
- Credit Score
- Risk Rating
- Customer Financial Summary
- Risk Analysis Charts
- AI Loan Recommendation
- PDF Report Generation

---

## Installation

Clone the repository

```bash
git clone https://github.com/Adeel-Khan11/credit-risk-prediction-system.git
```

Navigate to the project directory

```bash
cd credit-risk-prediction-system
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app/main.py
```

---

## Future Improvements

- MLflow integration
- Model monitoring
- Drift detection
- Docker support
- REST API
- User authentication
- Cloud deployment

---

## Acknowledgements

This project was completed as part of the Codebasics Data Science and Generative AI Bootcamp, where participants work on industry-inspired capstone projects based on real-world business scenarios.

The business case, Statement of Work (SOW), and project requirements were provided by Codebasics to simulate a client engagement between Lauki Finance and AtliQ AI.

Building upon these requirements, I independently designed, developed, optimized, and deployed the complete solution. This includes data preprocessing, feature engineering, model selection, Bayesian hyperparameter optimization, SHAP-based model explainability, an interactive Streamlit application, dynamic Plotly visualizations, AI-driven loan recommendations, and PDF report generation.

This project demonstrates an end-to-end machine learning workflow for solving a real-world credit risk assessment problem.

---

## Author

**Adeel Khan**

GitHub

https://github.com/Adeel-Khan11

LinkedIn

https://www.linkedin.com/in/adeel-khan-4a6b56308/

---
