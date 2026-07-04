import plotly.graph_objects as go
import plotly.express as px
def probability_gauge(probability):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=probability * 100,

            number={
                "suffix": "%",
                "font": {
                    "size": 42,
                    "color": "white"
                }
            },

            title={
                "text": "<b>Default Probability</b>",
                "font": {
                    "size": 24,
                    "color": "white"
                }
            },

            gauge={

                "axis": {
                    "range": [0,100],
                    "tickcolor":"white"
                },

                "bar":{
                    "color":"#00E5FF"
                },

                "steps":[

                    {
                        "range":[0,20],
                        "color":"#00C853"
                    },

                    {
                        "range":[20,50],
                        "color":"#FFD600"
                    },

                    {
                        "range":[50,100],
                        "color":"#D50000"
                    }

                ]
            }
        )
    )

    fig.update_layout(

        height=420,

        paper_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white")
    )

    return fig

def credit_score_gauge(score):

    fig = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=score,

            number={
                "font":{
                    "size":42,
                    "color":"white"
                }
            },

            title={
                "text":"<b>Credit Score</b>",
                "font":{
                    "size":24,
                    "color":"white"
                }
            },

            gauge={

                "axis":{
                    "range":[300,900]
                },

                "bar":{
                    "color":"#2962FF"
                },

                "steps":[

                    {
                        "range":[300,580],
                        "color":"#D50000"
                    },

                    {
                        "range":[580,670],
                        "color":"orange"
                    },

                    {
                        "range":[670,740],
                        "color":"gold"
                    },

                    {
                        "range":[740,900],
                        "color":"#00C853"
                    }

                ]
            }

        )
    )

    fig.update_layout(

        height=420,

        paper_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white")
    )

    return fig

def customer_chart(income, loan):

    fig = go.Figure()

    fig.add_bar(

        x=["Annual Income","Loan Amount"],

        y=[income,loan],

        text=[
            f"₹{income:,.0f}",
            f"₹{loan:,.0f}"
        ],

        textposition="outside"
    )

    fig.update_layout(

        title="Customer Financial Summary",

        height=420,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white"),

        xaxis=dict(showgrid=False),

        yaxis=dict(showgrid=True)
    )

    return fig

def radar_chart(
    delinquency,
    utilization,
    loan_income,
    avg_dpd
):

    categories = [
        "Delinquency",
        "Utilization",
        "Loan Ratio",
        "Avg DPD"
    ]

    values = [
        delinquency,
        utilization,
        min(loan_income * 100, 100),
        min(avg_dpd, 100)
    ]

    values += values[:1]
    categories += categories[:1]

    fig = go.Figure()

    fig.add_trace(

        go.Scatterpolar(

            r=values,

            theta=categories,

            fill="toself",

            line=dict(
                color="#00E5FF",
                width=3
            ),

            fillcolor="rgba(0,229,255,0.35)"
        )

    )

    fig.update_layout(

        title="Customer Risk Profile",

        polar=dict(

            bgcolor="rgba(0,0,0,0)",

            radialaxis=dict(

                visible=True,

                range=[0,100],

                gridcolor="gray",

                tickfont=dict(color="white")

            ),

            angularaxis=dict(

                tickfont=dict(color="white")

            )

        ),

        paper_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white"),

        height=450

    )

    return fig

def risk_pie(probability):

    low = round((1-probability)*100,2)

    high = round(probability*100,2)

    fig = px.pie(

        values=[low,high],

        names=[

            "Safe Probability",

            "Default Probability"

        ],

        hole=0.65,

        color_discrete_sequence=[

            "#00C853",

            "#D50000"

        ]

    )

    fig.update_traces(

        textinfo="percent+label"

    )

    fig.update_layout(

        title="Risk Distribution",

        paper_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white"),

        height=420,

        showlegend=True

    )

    return fig

def loan_health_meter(probability):

    health = (1-probability)*100

    fig = go.Figure(

        go.Indicator(

            mode="number+gauge",

            value=health,

            number={

                "suffix":"%",

                "font":{

                    "size":45,

                    "color":"white"

                }

            },

            title={

                "text":"Loan Health",

                "font":{

                    "size":24,

                    "color":"white"

                }

            },

            gauge={

                "axis":{

                    "range":[0,100]

                },

                "bar":{

                    "color":"#00C853"

                }

            }

        )

    )

    fig.update_layout(

        height=350,

        paper_bgcolor="rgba(0,0,0,0)"

    )

    return fig

def utilization_meter(utilization):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=utilization,

            number={

                "suffix":"%",

                "font":{

                    "size":40,

                    "color":"white"

                }

            },

            title={

                "text":"Credit Utilization"

            },

            gauge={

                "axis":{

                    "range":[0,100]

                },

                "bar":{

                    "color":"#2962FF"

                },

                "steps":[

                    {

                        "range":[0,30],

                        "color":"green"

                    },

                    {

                        "range":[30,70],

                        "color":"gold"

                    },

                    {

                        "range":[70,100],

                        "color":"red"

                    }

                ]

            }

        )

    )

    fig.update_layout(

        paper_bgcolor="rgba(0,0,0,0)",

        height=350

    )

    return fig

def comparison_chart(income, loan):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            name="Amount",

            x=["Income","Loan"],

            y=[income,loan]

        )

    )

    fig.update_layout(

        title="Income vs Loan Comparison",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white"),

        height=420

    )

    return fig

def risk_level_card(probability):

    if probability < 0.20:

        color = "#00C853"
        status = "LOW RISK"

    elif probability < 0.50:

        color = "#FFD600"
        status = "MEDIUM RISK"

    else:

        color = "#D50000"
        status = "HIGH RISK"

    fig = go.Figure()

    fig.add_trace(

        go.Indicator(

            mode="number",

            value=probability * 100,

            number={
                "suffix": "%",
                "font": {
                    "size": 45,
                    "color": color
                }
            },

            title={
                "text": f"<b>{status}</b>",
                "font": {
                    "size": 26,
                    "color": color
                }
            }

        )

    )

    fig.update_layout(

        height=250,

        paper_bgcolor="rgba(0,0,0,0)",

        margin=dict(l=20,r=20,t=40,b=20)

    )

    return fig


def loan_income_ratio_chart(income, loan):

    ratio = loan / income if income else 0

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=["Loan / Income"],

            y=[ratio],

            text=[f"{ratio:.2f}"],

            textposition="outside"

        )

    )

    fig.update_layout(

        title="Loan to Income Ratio",

        height=350,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white")

    )

    return fig


def credit_profile_chart(

    delinquency,

    utilization,

    dpd

):

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=[

                "Delinquency",

                "Utilization",

                "Avg DPD"

            ],

            y=[

                delinquency,

                utilization,

                dpd

            ],

            text=[

                f"{delinquency}%",

                f"{utilization}%",

                f"{dpd}"

            ],

            textposition="outside"

        )

    )

    fig.update_layout(

        title="Credit Behaviour",

        height=400,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white")

    )

    return fig


def score_meter(score):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=score,

            gauge={

                "axis":{

                    "range":[300,900]

                },

                "bar":{

                    "color":"#00E5FF"

                }

            }

        )

    )

    fig.update_layout(

        title="Overall Customer Score",

        paper_bgcolor="rgba(0,0,0,0)",

        font=dict(color="white"),

        height=350

    )

    return fig