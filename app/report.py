from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from datetime import datetime 
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import datetime

styles = getSampleStyleSheet()

# Create custom styles
styles.add(ParagraphStyle(
    name='Centered',
    parent=styles['Normal'],
    alignment=TA_CENTER,
    fontSize=10,
    textColor=colors.grey
))


def generate_pdf(filename, customer_data, prediction_data):
    """
    Generate a professional PDF report for credit risk assessment
    """

    # Create the document
    doc = SimpleDocTemplate(
        filename,
        pagesize=(8.5 * inch, 11 * inch),
        topMargin=0.5 * inch,
        bottomMargin=0.5 * inch
    )

    elements = []

    # ============================================================
    # HEADER SECTION
    # ============================================================

    # Title
    title = Paragraph(
        "<b><font size=24 color='#1B4D8C'>🏦 LAUKI FINANCE</font></b>",
        styles["Title"]
    )
    elements.append(title)

    elements.append(Spacer(1, 0.1 * inch))

    subtitle = Paragraph(
        "<b><font size=14 color='#4A5568'>AI Credit Risk Assessment Report</font></b>",
        styles["Heading2"]
    )
    elements.append(subtitle)

    elements.append(Spacer(1, 0.1 * inch))

    # Date and Time
    date_time = Paragraph(
        f"<font size=10 color='#718096'>Generated: {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}</font>",
        styles["Centered"]
    )
    elements.append(date_time)

    elements.append(Spacer(1, 0.3 * inch))

    # Divider line
    elements.append(Paragraph(
        "<hr color='#CBD5E0'/>",
        styles["Normal"]
    ))

    elements.append(Spacer(1, 0.3 * inch))

    # ============================================================
    # CUSTOMER INFORMATION SECTION
    # ============================================================

    # Section Header
    customer_header = Paragraph(
        "<b><font size=14 color='#1B4D8C'>📋 Customer Information</font></b>",
        styles["Heading2"]
    )
    elements.append(customer_header)

    elements.append(Spacer(1, 0.15 * inch))

    # Customer Table
    customer_table = [
        ["<b>Field</b>", "<b>Value</b>"],
        ["Age", str(customer_data["Age"])],
        ["Income", f"₹ {customer_data['Income']:,.0f}"],
        ["Loan Amount", f"₹ {customer_data['Loan Amount']:,.0f}"],
        ["Loan Tenure", f"{customer_data['Loan Tenure']} Months"],
        ["Residence", customer_data["Residence"]],
        ["Loan Purpose", customer_data["Loan Purpose"]],
        ["Loan Type", customer_data["Loan Type"]]
    ]

    table = Table(customer_table, colWidths=[2.5 * inch, 4 * inch])
    table.setStyle(
        TableStyle([
            # Header styling
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1B4D8C')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),

            # Grid
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),

            # Row styling
            ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#EDF2F7')),
            ('BACKGROUND', (1, 1), (1, -1), colors.white),

            # Padding
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),

            # Font
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
        ])
    )
    elements.append(table)

    elements.append(Spacer(1, 0.3 * inch))

    # ============================================================
    # PREDICTION RESULTS SECTION
    # ============================================================

    # Section Header
    prediction_header = Paragraph(
        "<b><font size=14 color='#1B4D8C'>📊 Prediction Results</font></b>",
        styles["Heading2"]
    )
    elements.append(prediction_header)

    elements.append(Spacer(1, 0.15 * inch))

    # Prediction Table
    prediction_table = [
        ["<b>Metric</b>", "<b>Value</b>"],
        ["Credit Score", str(prediction_data["Credit Score"])],
        ["Rating", prediction_data["Rating"]],
        ["Default Probability", prediction_data["Probability"]],
        ["Recommendation", prediction_data["Recommendation"]],
        ["Interest Rate", prediction_data["Interest"]]
    ]

    # Color code the recommendation
    rec_color = '#16A34A'  # Green
    if "Review" in prediction_data["Recommendation"]:
        rec_color = '#F59E0B'  # Orange
    elif "Rejected" in prediction_data["Recommendation"]:
        rec_color = '#DC2626'  # Red

    table2 = Table(prediction_table, colWidths=[2.5 * inch, 4 * inch])
    table2.setStyle(
        TableStyle([
            # Header styling
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1B4D8C')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),

            # Grid
            ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E0')),

            # Row styling
            ('BACKGROUND', (0, 1), (0, -1), colors.HexColor('#EDF2F7')),
            ('BACKGROUND', (1, 1), (1, -1), colors.white),

            # Special styling for Recommendation row
            ('BACKGROUND', (1, 4), (1, 4), colors.HexColor(rec_color)),
            ('TEXTCOLOR', (1, 4), (1, 4), colors.white),
            ('FONTNAME', (1, 4), (1, 4), 'Helvetica-Bold'),

            # Padding
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 12),
            ('RIGHTPADDING', (0, 0), (-1, -1), 12),

            # Font
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
        ])
    )
    elements.append(table2)

    elements.append(Spacer(1, 0.3 * inch))

    # ============================================================
    # AI RECOMMENDATION SECTION
    # ============================================================

    recommendation_header = Paragraph(
        "<b><font size=14 color='#1B4D8C'>🤖 AI Recommendation</font></b>",
        styles["Heading2"]
    )
    elements.append(recommendation_header)

    elements.append(Spacer(1, 0.1 * inch))

    # Get recommendation message based on status
    if prediction_data["Recommendation"] == "Loan Approved":
        rec_message = """
        <b>✅ APPROVED - Low Credit Risk</b><br/><br/>
        The customer presents a very low probability of default and is 
        recommended for loan approval with premium interest rates.
        <br/><br/>
        <b>Key Factors:</b><br/>
        • Excellent credit score<br/>
        • Strong repayment behaviour<br/>
        • Low debt-to-income ratio<br/>
        • Stable financial profile
        """
    elif "Review" in prediction_data["Recommendation"]:
        rec_message = """
        <b>⚠️ MANUAL REVIEW REQUIRED - Medium Credit Risk</b><br/><br/>
        The customer presents a moderate credit risk. Additional verification 
        is recommended before making a final decision.
        <br/><br/>
        <b>Suggested Actions:</b><br/>
        • Verify income documents<br/>
        • Review bank statements<br/>
        • Check existing liabilities<br/>
        • Consider collateral options
        """
    else:
        rec_message = """
        <b>❌ REJECTED - High Credit Risk</b><br/><br/>
        The customer presents a high probability of default based on 
        their financial profile and credit history.
        <br/><br/>
        <b>Reasons:</b><br/>
        • Poor credit history<br/>
        • High debt-to-income ratio<br/>
        • Late repayment patterns<br/>
        • Unsuitable for unsecured lending
        """

    recommendation = Paragraph(
        rec_message,
        styles["BodyText"]
    )
    elements.append(recommendation)

    elements.append(Spacer(1, 0.3 * inch))

    # ============================================================
    # DISCLAIMER SECTION
    # ============================================================

    elements.append(Paragraph(
        "<hr color='#CBD5E0'/>",
        styles["Normal"]
    ))

    elements.append(Spacer(1, 0.1 * inch))

    disclaimer = Paragraph(
        """
        <b><font size=9 color='#718096'>Disclaimer</font></b><br/>
        <font size=8 color='#A0AEC0'>
        This report is generated automatically by the Lauki Finance AI Platform 
        and should be used as a decision-support tool. Final lending decisions 
        should consider additional factors and human judgment.
        </font>
        """,
        styles["Normal"]
    )
    elements.append(disclaimer)

    elements.append(Spacer(1, 0.2 * inch))

    # ============================================================
    # FOOTER
    # ============================================================

    footer = Paragraph(
        f"""
        <font size=8 color='#A0AEC0'>
        Generated by <b>Lauki Finance AI Platform</b> | 
        Report ID: {datetime.datetime.now().strftime('%Y%m%d%H%M%S')} | 
        © 2026 Lauki Finance
        </font>
        """,
        styles["Centered"]
    )
    elements.append(footer)

    # Build the document
    doc.build(elements)

    return filename