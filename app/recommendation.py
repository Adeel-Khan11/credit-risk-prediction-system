def generate_recommendation(probability, credit_score):
    """
    AI Recommendation Engine

    Input:
        probability -> Default Probability (0-1)
        credit_score -> Credit Score

    Output:
        Dictionary containing:
            Status
            Color
            Interest Rate
            Confidence
            Loan Product
            Risk
            Message
            Next Action
    """

    probability_percent = probability * 100

    # =====================================================
    # LOW RISK
    # =====================================================

    if probability < 0.20 and credit_score >= 750:
        return {
            "status": "Loan Approved",
            "color": "green",
            "interest": "8.5%",
            "confidence": "98%",
            "risk": "Low",
            "product": "Gold Personal Loan",
            "next_action": "Auto Approval",
            "message": "Excellent credit profile with very low probability of default. Strong repayment behaviour. Eligible for premium interest rates. Suitable for higher loan limits."
        }

    # =====================================================
    # GOOD CUSTOMER
    # =====================================================

    elif probability < 0.35 and credit_score >= 700:
        return {
            "status": "Approved with Review",
            "color": "green",
            "interest": "9.5%",
            "confidence": "94%",
            "risk": "Low-Medium",
            "product": "Standard Personal Loan",
            "next_action": "Quick Verification",
            "message": "Customer has a good financial profile with low repayment risk. Minor verification recommended. Suitable for standard lending."
        }

    # =====================================================
    # MEDIUM RISK
    # =====================================================

    elif probability < 0.55:
        return {
            "status": "Manual Review Required",
            "color": "orange",
            "interest": "12.5%",
            "confidence": "86%",
            "risk": "Medium",
            "product": "Secured Loan",
            "next_action": "Income Verification",
            "message": "Moderate default risk detected. Verify employment and check bank statements. Consider collateral and review existing liabilities."
        }

    # =====================================================
    # HIGH RISK
    # =====================================================

    else:
        return {
            "status": "Loan Rejected",
            "color": "red",
            "interest": "Not Eligible",
            "confidence": "99%",
            "risk": "High",
            "product": "None",
            "next_action": "Reject Application",
            "message": "Very high probability of default with poor repayment behaviour. High financial risk. Not recommended for unsecured lending. Improve credit profile before reapplying."
        }