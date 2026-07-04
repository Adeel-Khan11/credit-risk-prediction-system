import os
import streamlit as st
from report import generate_pdf
from prediction_helper import predict
from recommendation import generate_recommendation
import time
import tempfile
from charts import (
    probability_gauge,
    credit_score_gauge,
    customer_chart,
    radar_chart,
    risk_pie
)
from datetime import datetime
# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Lauki Finance - Credit Risk Assessment",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================
# LOAD CSS
# ======================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

css_path = os.path.join(
    BASE_DIR,
    "assets",
    "style.css"
)

try:
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ======================================================
# SIDEBAR - CLEAN AND MINIMAL
# ======================================================

with st.sidebar:
    # Logo and Title
    st.markdown("""
    <div style="text-align: center; padding: 10px 0;">
        <h1 style="font-size: 48px; margin: 0;">🏦</h1>
        <h2 style="color: white; margin: 5px 0;">Lauki Finance</h2>
        <p style="color: #D5E5FF; font-size: 13px;">AI-Powered Credit Risk Assessment</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ======================================================
    # PROJECT INTRODUCTION
    # ======================================================

    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 10px; padding: 15px; border-left: 4px solid #667eea;">
        <strong style="color: white;">📋 About Lauki Finance</strong><br><br>
        <span style="color: #D5E5FF; font-size: 13px;">AI-powered credit risk assessment platform for real-time lending decisions using machine learning. Helps financial institutions make faster, data-driven decisions.</span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ======================================================
    # KEY FEATURES
    # ======================================================

    st.markdown("""
    <div style="background: rgba(255,255,255,0.05); border-radius: 10px; padding: 15px; border-left: 4px solid #667eea;">
        <strong style="color: white;">🎯 Key Features</strong><br><br>
        <span style="color: #D5E5FF; font-size: 13px;">
        • Real-time credit risk scoring<br>
        • Default probability prediction<br>
        • Automated loan eligibility<br>
        • AI-powered recommendations<br>
        • Interactive data visualization
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ======================================================
    # SYSTEM STATUS
    # ======================================================

    st.markdown("### 🟢 System Status")
    st.success("Model: Online")
    st.caption("🔄 Predictions: Real-time")
    st.caption("🔒 Data Encryption: Enabled")

    st.divider()

    # ======================================================
    # FOOTER
    # ======================================================

    st.caption("© 2026 Lauki Finance")
    st.caption("Built with ❤️ using Streamlit")

# ======================================================
# HERO SECTION
# ======================================================

st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; text-align: center;">

<h1>🏦 Lauki Finance</h1>

<h3>AI Powered Credit Risk Assessment Dashboard</h3>

<p>Professional Banking Analytics Platform</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ======================================================
# KPI PLACEHOLDER
# ======================================================

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Credit Score",
        "--"
    )

with k2:
    st.metric(
        "Default %",
        "--"
    )

with k3:
    st.metric(
        "Risk Level",
        "--"
    )

with k4:
    st.metric(
        "Recommendation",
        "--"
    )

st.divider()

# ======================================================
# CUSTOMER INFORMATION
# ======================================================

st.markdown("## 👤 Customer Information")

c1, c2, c3 = st.columns(3)

with c1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=28
    )

with c2:
    income = st.number_input(
        "Annual Income (₹)",
        value=1200000,
        step=100000
    )

with c3:
    loan_amount = st.number_input(
        "Loan Amount (₹)",
        value=2500000,
        step=100000
    )

# ======================================================
# LOAN DETAILS
# ======================================================

st.markdown("## 🏦 Loan Details")

c1, c2, c3 = st.columns(3)

with c1:
    loan_tenure_months = st.number_input(
        "Loan Tenure (Months)",
        value=36,
        min_value=6,
        max_value=360
    )

with c2:
    avg_dpd_per_delinquency = st.number_input(
        "Average DPD (Days Past Due)",
        value=20,
        min_value=0,
        max_value=90
    )

with c3:
    num_open_accounts = st.selectbox(
        "Open Accounts",
        [1, 2, 3, 4, 5, 6, 7, 8],
        index=2
    )

# ======================================================
# CREDIT PROFILE
# ======================================================

st.markdown("## 📈 Credit Behaviour")

c1, c2, c3 = st.columns(3)

with c1:
    delinquency_ratio = st.slider(
        "Delinquency Ratio (%)",
        0,
        100,
        30
    )

with c2:
    credit_utilization_ratio = st.slider(
        "Credit Utilization (%)",
        0,
        100,
        30
    )

loan_to_income = (
    loan_amount / income
    if income and income > 0 else 0
)

with c3:
    st.metric(
        "Loan / Income Ratio",
        f"{loan_to_income:.2f}"
    )

# ======================================================
# ADDITIONAL DETAILS
# ======================================================

st.markdown("## 🏠 Additional Details")

c1, c2, c3 = st.columns(3)

with c1:
    residence_type = st.selectbox(
        "Residence Type",
        [
            "Owned",
            "Mortgage",
            "Rented"
        ]
    )

with c2:
    loan_purpose = st.selectbox(
        "Loan Purpose",
        [
            "Home",
            "Education",
            "Auto",
            "Personal",
            "Business",
            "Debt Consolidation"
        ]
    )

with c3:
    loan_type = st.selectbox(
        "Loan Type",
        [
            "Secured",
            "Unsecured"
        ]
    )

st.write("")
st.write("")

predict_btn = st.button(
    "🚀 Analyze Customer",
    use_container_width=True,
    type="primary"
)

# ======================================================
# PREDICTION STARTS HERE
# ======================================================

if predict_btn:
    # Validate inputs
    if income <= 0:
        st.error("❌ Annual Income must be greater than 0")
        st.stop()

    if loan_amount <= 0:
        st.error("❌ Loan Amount must be greater than 0")
        st.stop()

    # ======================================================
    # LOADING & PREDICTION
    # ======================================================
    start = time.time()
    with st.spinner("Analyzing customer profile..."):

        probability, credit_score, rating = predict(
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
        )

    st.success("✅ Analysis Completed Successfully")
    end = time.time()
    response_time = end - start

    st.caption(
        f"Prediction completed in {response_time:.3f} seconds"
    )

    # ======================================================
    # UPDATE KPI CARDS
    # ======================================================

    st.write("### 💳 Credit Score Progress")

    st.progress(
        min(credit_score / 900, 1.0)
    )

    st.caption(
        f"{credit_score:.0f} / 900"
    )

    st.write("### ⚠ Default Probability")

    st.progress(probability)

    st.caption(
        f"{probability:.2%}"
    )

    eligibility = max(
        0,
        100 - probability * 100
    )

    st.write("### ✅ Loan Eligibility")

    st.progress(
        eligibility / 100
    )

    st.caption(
        f"{eligibility:.0f}%"
    )

    st.divider()

    st.subheader("📊 Executive Summary")

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric(
            "Credit Score",
            int(credit_score),
            delta=None
        )

    with k2:
        st.metric(
            "Default Probability",
            f"{probability:.2%}"
        )

    with k3:
        if rating == "Excellent":
            st.success("🟢 Excellent")
        elif rating == "Very Good":
            st.success("🟢 Very Good")
        elif rating == "Good":
            st.info("🔵 Good")
        elif rating == "Average":
            st.warning("🟠 Average")
        else:
            st.error("🔴 Poor")

    with k4:
        if probability < 0.20:
            st.success("✅ APPROVE")
        elif probability < 0.50:
            st.warning("⚠️ REVIEW")
        else:
            st.error("❌ REJECT")

    # ======================================================
    # GAUGE CHARTS
    # ======================================================

    st.divider()

    st.subheader("📈 Credit Dashboard")

    left, right = st.columns(2)

    with left:
        try:
            st.plotly_chart(
                probability_gauge(probability),
                use_container_width=True
            )
        except:
            st.warning("⚠️ Chart not available")

    with right:
        try:
            st.plotly_chart(
                credit_score_gauge(credit_score),
                use_container_width=True
            )
        except:
            st.warning("⚠️ Chart not available")

    # ======================================================
    # FINANCIAL SUMMARY
    # ======================================================

    st.divider()

    st.subheader("💰 Financial Summary")

    try:
        st.plotly_chart(
            customer_chart(
                income,
                loan_amount
            ),
            use_container_width=True
        )
    except:
        st.warning("⚠️ Chart not available")

    # ======================================================
    # AI RECOMMENDATION
    # ======================================================

    st.divider()

    st.subheader("🤖 AI Recommendation")

    try:
        recommendation = generate_recommendation(
            probability,
            credit_score
        )

        # Beautiful Risk Banner
        if recommendation["color"] == "green":
            st.markdown("""
            <div style="background:#16A34A; padding:18px; border-radius:15px; text-align:center; color:white; font-size:22px; font-weight:bold;">
            ✅ LOW CREDIT RISK
            </div>
            """, unsafe_allow_html=True)
        elif recommendation["color"] == "orange":
            st.markdown("""
            <div style="background:#F59E0B; padding:18px; border-radius:15px; text-align:center; color:white; font-size:22px; font-weight:bold;">
            ⚠ MEDIUM CREDIT RISK
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background:#DC2626; padding:18px; border-radius:15px; text-align:center; color:white; font-size:22px; font-weight:bold;">
            ❌ HIGH CREDIT RISK
            </div>
            """, unsafe_allow_html=True)

        # Recommendation Cards
        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Suggested Interest",
                recommendation["interest"]
            )

        with col2:
            st.metric(
                "Risk Category",
                rating
            )

        # Display message as clean bullet points
        message = recommendation["message"]
        points = [p.strip() for p in message.split('.') if p.strip()]

        st.markdown("### 📋 Recommendation Details")
        for point in points:
            st.markdown(f"• {point}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Confidence",
                recommendation["confidence"]
            )
            st.metric(
                "Loan Product",
                recommendation["product"]
            )

        with col2:
            st.metric(
                "Risk Level",
                recommendation["risk"]
            )
            st.metric(
                "Next Action",
                recommendation["next_action"]
            )

    except Exception as e:
        st.error(f"❌ Error generating recommendation: {str(e)}")

    # ======================================================
    # RISK ANALYSIS
    # ======================================================

    st.divider()

    st.subheader("📉 Risk Analysis")

    left, right = st.columns(2)

    with left:
        try:
            st.plotly_chart(
                risk_pie(probability),
                use_container_width=True
            )
        except:
            st.warning("⚠️ Chart not available")

    with right:
        try:
            st.plotly_chart(
                radar_chart(
                    delinquency_ratio,
                    credit_utilization_ratio,
                    loan_to_income,
                    avg_dpd_per_delinquency
                ),
                use_container_width=True
            )
        except:
            st.warning("⚠️ Chart not available")

    # ======================================================
    # CUSTOMER PROFILE
    # ======================================================

    st.divider()

    st.subheader("📄 Customer Profile")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 👤 Personal Information")
        st.write(f"**Age:** {age} Years")
        st.write(f"**Residence:** {residence_type}")
        st.write(f"**Open Loan Accounts:** {num_open_accounts}")
        st.write(f"**Loan Purpose:** {loan_purpose}")
        st.write(f"**Loan Type:** {loan_type}")

    with col2:
        st.markdown("### 💰 Financial Information")
        st.write(f"**Annual Income:** ₹ {income:,.0f}")
        st.write(f"**Loan Amount:** ₹ {loan_amount:,.0f}")
        st.write(f"**Loan Tenure:** {loan_tenure_months} Months")
        st.write(f"**Loan / Income Ratio:** {loan_to_income:.2f}")
        st.write(f"**Average DPD:** {avg_dpd_per_delinquency}")

    # ======================================================
    # MODEL PREDICTION SUMMARY
    # ======================================================

    st.divider()

    st.subheader("🎯 Model Prediction Summary")

    try:
        summary = {
            "Default Probability": f"{probability:.2%}",
            "Credit Score": int(credit_score),
            "Credit Rating": rating,
            "Suggested Interest": recommendation["interest"],
            "Recommendation": recommendation["status"]
        }
    except:
        summary = {
            "Default Probability": f"{probability:.2%}",
            "Credit Score": int(credit_score),
            "Credit Rating": rating,
        }

    st.json(summary)

    # ======================================================
    # DECISION BOX
    # ======================================================

    st.divider()

    if probability < 0.20:
        st.success("""
        ### ✅ Loan Approval Recommendation

        The customer presents **Low Credit Risk**.

        **Recommended Action:**
        ✔ Approve Loan
        ✔ Offer Premium Interest Rate
        ✔ Eligible for Higher Credit Limit
        """)
    elif probability < 0.50:
        st.warning("""
        ### ⚠ Manual Review Required

        The customer presents **Medium Credit Risk**.

        **Recommended Action:**
        • Verify Documents
        • Review Banking History
        • Assess Additional Income Sources
        """)
    else:
        st.error("""
        ### ❌ High Credit Risk

        The customer has a high probability of default.

        **Recommended Action:**
        • Reject Application
        or
        • Request Collateral
        """)

    # ======================================================
    # DOWNLOAD PDF REPORT - USING TEMPORARY FILE
    # ======================================================

    st.divider()

    st.subheader("📥 Download Professional Report")

    try:
        customer_data = {
            "Age": age,
            "Income": income,
            "Loan Amount": loan_amount,
            "Loan Tenure": loan_tenure_months,
            "Residence": residence_type,
            "Loan Purpose": loan_purpose,
            "Loan Type": loan_type
        }

        prediction_data = {
            "Credit Score": int(credit_score),
            "Rating": rating,
            "Probability": f"{probability:.2%}",
            "Recommendation": recommendation["status"],
            "Interest": recommendation["interest"]
        }

        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            temp_pdf_path = tmp_file.name

        # Generate PDF to temporary location
        generate_pdf(temp_pdf_path, customer_data, prediction_data)

        # Read and provide download
        with open(temp_pdf_path, "rb") as pdf:
            st.download_button(
                label="📄 Download Professional PDF Report",
                data=pdf,
                file_name=f"Credit_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        # Clean up temporary file after download
        try:
            os.unlink(temp_pdf_path)
        except:
            pass

    except Exception as e:
        st.error(f"❌ Error generating PDF: {str(e)}")

    # ======================================================
    # THANK YOU
    # ======================================================

    st.divider()

    st.markdown(
        """
    <div style="text-align:center;padding:25px;">

    <h2>🏦 Lauki Finance</h2>

    <h4>AI Powered Credit Risk Assessment</h4>

    <p>
    Built using
    <b>Python</b>,
    <b>Streamlit</b>,
    <b>XGBoost</b>,
    <b>Plotly</b>
    and
    <b>Machine Learning</b>.
    </p>

    </div>
    """,
        unsafe_allow_html=True
    )