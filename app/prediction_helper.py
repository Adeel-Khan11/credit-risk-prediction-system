import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime
# =====================================================
# BASE DIRECTORY - FIXED PATH
# =====================================================

# Get the directory where this file is located (app folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level to get the project root
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Your model is at: artifacts/model/model_data.joblib (relative to project root)
MODEL_PATH = os.path.join(PROJECT_ROOT, "artifacts", "model", "model_data.joblib")

# Alternative: Use absolute path directly
# MODEL_PATH = r"C:\Users\Adeel khan\Desktop\Bootcamp\machine learning\Project 2\Project2_StreamlitApp_Resources\artifacts\model\model_data.joblib"

# Print debug info to verify
print(f"DEBUG: Project Root: {PROJECT_ROOT}")
print(f"DEBUG: Looking for model at: {MODEL_PATH}")
print(f"DEBUG: File exists: {os.path.exists(MODEL_PATH)}")

# =====================================================
# LAZY LOADING - Load model only when needed
# =====================================================

_model_data = None
_model = None
_scaler = None
_features = None
_cols_to_scale = None


def load_model_data():
    """Load model data only when needed"""
    global _model_data, _model, _scaler, _features, _cols_to_scale

    if _model_data is None:
        try:
            if os.path.exists(MODEL_PATH):
                _model_data = joblib.load(MODEL_PATH)
                _model = _model_data['model']
                _scaler = _model_data['scaler']
                _features = _model_data['features']
                _cols_to_scale = _model_data['cols_to_scale']
                st.success("✅ Model loaded successfully!")
                return True
            else:
                st.warning(f"""
                ⚠️ Model file not found at: {MODEL_PATH}

                **Please verify:**
                1. The model exists at this location
                2. The file name is exactly 'model_data.joblib'
                3. You have read permissions
                """)
                return False
        except Exception as e:
            st.error(f"❌ Error loading model: {str(e)}")
            return False
    return True


def get_model_components():
    """Get model components"""
    if load_model_data():
        return _model, _scaler, _features, _cols_to_scale
    return None, None, None, None


# =====================================================
# PREPARE INPUT - MATCHING YOUR WORKING VERSION
# =====================================================

def prepare_input(age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
                  delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                  residence_type, loan_purpose, loan_type):
    """
    Prepare input data with dummy values for missing features
    This matches your working file structure
    """

    # Create a dictionary with input values and dummy values for missing features
    input_data = {
        'age': age,
        'loan_tenure_months': loan_tenure_months,
        'number_of_open_accounts': num_open_accounts,
        'credit_utilization_ratio': credit_utilization_ratio,
        'loan_to_income': loan_amount / income if income > 0 else 0,
        'delinquency_ratio': delinquency_ratio,
        'avg_dpd_per_delinquency': avg_dpd_per_delinquency,
        'residence_type_Owned': 1 if residence_type == 'Owned' else 0,
        'residence_type_Rented': 1 if residence_type == 'Rented' else 0,
        'loan_purpose_Education': 1 if loan_purpose == 'Education' else 0,
        'loan_purpose_Home': 1 if loan_purpose == 'Home' else 0,
        'loan_purpose_Personal': 1 if loan_purpose == 'Personal' else 0,
        'loan_type_Unsecured': 1 if loan_type == 'Unsecured' else 0,
        # Additional dummy fields for scaling purpose
        'number_of_dependants': 1,
        'years_at_current_address': 1,
        'zipcode': 1,
        'sanction_amount': 1,
        'processing_fee': 1,
        'gst': 1,
        'net_disbursement': 1,
        'principal_outstanding': 1,
        'bank_balance_at_application': 1,
        'number_of_closed_accounts': 1,
        'enquiry_count': 1
    }

    # Create DataFrame
    df = pd.DataFrame([input_data])

    # Get model components
    model, scaler, features, cols_to_scale = get_model_components()

    if scaler is not None and cols_to_scale is not None:
        # Scale the required columns
        df[cols_to_scale] = scaler.transform(df[cols_to_scale])

    if features is not None:
        # Ensure the DataFrame contains only the features expected by the model
        df = df[features]

    return df


# =====================================================
# CALCULATE CREDIT SCORE
# =====================================================

def calculate_credit_score(input_df, base_score=300, scale_length=600):
    """
    Calculate credit score from model predictions
    """
    model, scaler, features, cols_to_scale = get_model_components()

    if model is None:
        return None, None, None

    try:
        # Get prediction
        x = np.dot(input_df.values, model.coef_.T) + model.intercept_

        # Apply logistic function to calculate probability
        default_probability = 1 / (1 + np.exp(-x))
        non_default_probability = 1 - default_probability

        # Convert to credit score (300-900)
        credit_score = base_score + non_default_probability.flatten() * scale_length

        # Determine rating
        def get_rating(score):
            if 300 <= score < 500:
                return 'Poor'
            elif 500 <= score < 650:
                return 'Average'
            elif 650 <= score < 750:
                return 'Good'
            elif 750 <= score <= 900:
                return 'Excellent'
            else:
                return 'Undefined'

        rating = get_rating(credit_score[0])

        return default_probability.flatten()[0], int(credit_score[0]), rating
    except Exception as e:
        st.error(f"❌ Error calculating credit score: {str(e)}")
        return None, None, None


# =====================================================
# FALLBACK PREDICTION (When model not available)
# =====================================================

def fallback_predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_delinquency,
        delinquency_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
):
    """Simple rule-based prediction when model is not available"""

    risk_score = 0

    # Age factor
    if age < 25:
        risk_score += 20
    elif age < 35:
        risk_score += 10
    elif age < 50:
        risk_score += 5

    # Income factor
    if income < 500000:
        risk_score += 25
    elif income < 1000000:
        risk_score += 15
    elif income < 2000000:
        risk_score += 5

    # Loan to income ratio
    loan_to_income = loan_amount / income if income and income > 0 else 5
    if loan_to_income > 3:
        risk_score += 20
    elif loan_to_income > 2:
        risk_score += 10
    elif loan_to_income > 1:
        risk_score += 5

    # DPD
    if avg_dpd_per_delinquency > 60:
        risk_score += 25
    elif avg_dpd_per_delinquency > 30:
        risk_score += 15
    elif avg_dpd_per_delinquency > 10:
        risk_score += 5

    # Delinquency ratio
    if delinquency_ratio > 70:
        risk_score += 20
    elif delinquency_ratio > 50:
        risk_score += 10
    elif delinquency_ratio > 30:
        risk_score += 5

    # Credit utilization
    if credit_utilization_ratio > 80:
        risk_score += 15
    elif credit_utilization_ratio > 60:
        risk_score += 10
    elif credit_utilization_ratio > 40:
        risk_score += 5

    # Residence
    if residence_type == "Rented":
        risk_score += 10
    elif residence_type == "Mortgage":
        risk_score += 5

    # Loan type
    if loan_type == "Unsecured": risk_score += 10

    risk_score = min(100, risk_score)
    probability = risk_score / 100

    # Add slight randomness for realism
    probability = max(0, min(1, probability + np.random.normal(0, 0.03)))

    # Calculate credit score
    base_score = 300
    scale_length = 600
    non_default_probability = 1 - probability
    credit_score = base_score + non_default_probability * scale_length
    credit_score = int(max(300, min(900, credit_score)))

    # Get rating
    if credit_score >= 750:
        rating = "Excellent"
    elif credit_score >= 650:
        rating = "Good"
    elif credit_score >= 500:
        rating = "Average"
    else:
        rating = "Poor"

    return probability, credit_score, rating


# =====================================================
# MAIN PREDICT FUNCTION
# =====================================================

def predict(
        age,
        income,
        loan_amount,
        loan_tenure_months,
        avg_dpd_per_delinquency,
        delinquency_ratio,
        credit_utilization_ratio,
        num_open_accounts,
        residence_type,
        loan_purpose,
        loan_type
):
    """
    Predict default probability and credit score
    """

    # Check if model is loaded
    model, scaler, features, cols_to_scale = get_model_components()

    # If model not available, use fallback
    if model is None:
        st.info("ℹ️ Using fallback prediction (model not available)")
        return fallback_predict(
            age, income, loan_amount, loan_tenure_months,
            avg_dpd_per_delinquency, delinquency_ratio,
            credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type
        )

    try:
        # Prepare input data
        input_df = prepare_input(
            age, income, loan_amount, loan_tenure_months,
            avg_dpd_per_delinquency, delinquency_ratio,
            credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type
        )

        # Calculate credit score
        probability, credit_score, rating = calculate_credit_score(input_df)

        if probability is None:
            return fallback_predict(
                age, income, loan_amount, loan_tenure_months,
                avg_dpd_per_delinquency, delinquency_ratio,
                credit_utilization_ratio, num_open_accounts,
                residence_type, loan_purpose, loan_type
            )

        return probability, credit_score, rating

    except Exception as e:
        st.error(f"❌ Prediction error: {str(e)}")
        return fallback_predict(
            age, income, loan_amount, loan_tenure_months,
            avg_dpd_per_delinquency, delinquency_ratio,
            credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type
        )


# =====================================================
# DEBUG FUNCTION - Check model structure
# =====================================================

def debug_model():
    """Debug function to check model structure"""
    print("=" * 50)
    print("🔍 DEBUGGING MODEL...")
    print("=" * 50)

    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Looking for model at: {MODEL_PATH}")
    print(f"File exists: {os.path.exists(MODEL_PATH)}")

    if os.path.exists(MODEL_PATH):
        size = os.path.getsize(MODEL_PATH) / (1024 * 1024)
        print(f"File size: {size:.2f} MB")

    print("\n" + "=" * 50)

    model, scaler, features, cols_to_scale = get_model_components()

    if model is not None:
        print("✅ Model loaded successfully!")
        print(f"Model type: {type(model).__name__}")
        if features:
            print(f"Features: {features}")
        if cols_to_scale:
            print(f"Columns to scale: {cols_to_scale}")
        return True
    else:
        print("❌ Model not loaded!")
        return False


# =====================================================
# TEST FUNCTION
# =====================================================

if __name__ == "__main__":
    # Debug first
    debug_model()

    print("\n" + "=" * 50)
    print("🧪 Testing Prediction...")
    print("=" * 50)

    # Test the prediction
    result = predict(
        age=28,
        income=1200000,
        loan_amount=2500000,
        loan_tenure_months=36,
        avg_dpd_per_delinquency=20,
        delinquency_ratio=30,
        credit_utilization_ratio=30,
        num_open_accounts=3,
        residence_type="Owned",
        loan_purpose="Home",
        loan_type="Secured"
    )
    print(f"Probability: {result[0]:.2%}")
    print(f"Credit Score: {result[1]:.0f}")
    print(f"Rating: {result[2]}")