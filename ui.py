import streamlit as st
import requests

# ── Page config ────────────────────────────────────────────────────
st.set_page_config(page_title="AttritionGuard", page_icon="👥")
st.title("👥 Attrition Guard")
st.caption("Predict employee attrition risk")

# ── API config ─────────────────────────────────────────────────────
API_URL = "http://localhost:8001"

MODEL_CONFIG = {
    "local":  f"{API_URL}/predict/local",
    "mlflow": f"{API_URL}/predict/mlflow",
}

# ── Model selector ─────────────────────────────────────────────────
st.subheader("Model Source")
model_choice = st.radio(
    "MODEL",
    options=["local", "mlflow"],
    horizontal=True
)
st.code(f"MODEL    = {model_choice}\nendpoint = {MODEL_CONFIG[model_choice]}", language="bash")

st.divider()

# ── Input form ─────────────────────────────────────────────────────
st.subheader("Employee Details")

col1, col2, col3 = st.columns(3)

with col1:
    Age                     = st.number_input("Age",                   min_value=18,  max_value=65,    value=35)
    MonthlyIncome           = st.number_input("Monthly Income",        min_value=1,   max_value=100000, value=5000)
    TotalWorkingYears       = st.number_input("Total Working Years",   min_value=0,   max_value=40,    value=8)
    YearsAtCompany          = st.number_input("Years at Company",      min_value=0,   max_value=40,    value=3)
    YearsInCurrentRole      = st.number_input("Years in Current Role", min_value=0,   max_value=20,    value=2)
    YearsSinceLastPromotion = st.number_input("Years Since Promotion", min_value=0,   max_value=20,    value=1)
    YearsWithCurrManager    = st.number_input("Years with Manager",    min_value=0,   max_value=20,    value=2)
    NumCompaniesWorked      = st.number_input("Num Companies Worked",  min_value=0,   max_value=10,    value=3)
    TrainingTimesLastYear   = st.number_input("Trainings Last Year",   min_value=0,   max_value=10,    value=2)
    PercentSalaryHike       = st.number_input("Percent Salary Hike",   min_value=0,   max_value=100,   value=13)

with col2:
    JobSatisfaction          = st.slider("Job Satisfaction",          min_value=1, max_value=4, value=2)
    EnvironmentSatisfaction  = st.slider("Environment Satisfaction",  min_value=1, max_value=4, value=2)
    RelationshipSatisfaction = st.slider("Relationship Satisfaction", min_value=1, max_value=4, value=2)
    WorkLifeBalance          = st.slider("Work Life Balance",         min_value=1, max_value=4, value=2)
    JobInvolvement           = st.slider("Job Involvement",           min_value=1, max_value=4, value=3)
    PerformanceRating        = st.slider("Performance Rating",        min_value=1, max_value=4, value=3)
    Education                = st.slider("Education",                 min_value=1, max_value=5, value=3)
    JobLevel                 = st.slider("Job Level",                 min_value=1, max_value=5, value=2)
    StockOptionLevel         = st.slider("Stock Option Level",        min_value=0, max_value=3, value=1)

with col3:
    OverTime       = st.selectbox("OverTime",        options=[0, 1],    index=1,  format_func=lambda x: "Yes" if x == 1 else "No")
    Gender         = st.selectbox("Gender",          options=[0, 1],    index=1,  format_func=lambda x: "Male" if x == 1 else "Female")
    MaritalStatus  = st.selectbox("Marital Status",  options=[0, 1, 2], index=0,  format_func=lambda x: ["Single", "Married", "Divorced"][x])
    BusinessTravel = st.selectbox("Business Travel", options=[0, 1, 2], index=1,  format_func=lambda x: ["Non-Travel", "Travel Rarely", "Travel Frequently"][x])
    Department     = st.selectbox("Department",      options=[0, 1, 2], index=1,  format_func=lambda x: ["HR", "R&D", "Sales"][x])
    EducationField = st.selectbox("Education Field", options=[0, 1, 2, 3, 4, 5], index=1, format_func=lambda x: ["HR", "Life Sciences", "Marketing", "Medical", "Other", "Technical"][x])
    JobRole        = st.selectbox("Job Role",        options=list(range(9)), index=2, format_func=lambda x: ["Healthcare Rep", "HR", "Lab Technician", "Manager", "Mfg Director", "Research Director", "Research Scientist", "Sales Exec", "Sales Rep"][x])
    DailyRate      = st.number_input("Daily Rate",   min_value=1, max_value=2000,  value=800)
    HourlyRate     = st.number_input("Hourly Rate",  min_value=1, max_value=200,   value=60)
    MonthlyRate    = st.number_input("Monthly Rate", min_value=1, max_value=30000, value=15000)
    DistanceFromHome = st.number_input("Distance From Home", min_value=0, max_value=100, value=10)

# ── Predict button ─────────────────────────────────────────────────
st.divider()
if st.button("Predict Attrition Risk", type="primary", use_container_width=True):

    payload = {
        "Age":                     Age,
        "BusinessTravel":          BusinessTravel,
        "DailyRate":               DailyRate,
        "Department":              Department,
        "DistanceFromHome":        DistanceFromHome,
        "Education":               Education,
        "EducationField":          EducationField,
        "EnvironmentSatisfaction": EnvironmentSatisfaction,
        "Gender":                  Gender,
        "HourlyRate":              HourlyRate,
        "JobInvolvement":          JobInvolvement,
        "JobLevel":                JobLevel,
        "JobRole":                 JobRole,
        "JobSatisfaction":         JobSatisfaction,
        "MaritalStatus":           MaritalStatus,
        "MonthlyIncome":           MonthlyIncome,
        "MonthlyRate":             MonthlyRate,
        "NumCompaniesWorked":      NumCompaniesWorked,
        "OverTime":                OverTime,
        "PercentSalaryHike":       PercentSalaryHike,
        "PerformanceRating":       PerformanceRating,
        "RelationshipSatisfaction":RelationshipSatisfaction,
        "StockOptionLevel":        StockOptionLevel,
        "TotalWorkingYears":       TotalWorkingYears,
        "TrainingTimesLastYear":   TrainingTimesLastYear,
        "WorkLifeBalance":         WorkLifeBalance,
        "YearsAtCompany":          YearsAtCompany,
        "YearsInCurrentRole":      YearsInCurrentRole,
        "YearsSinceLastPromotion": YearsSinceLastPromotion,
        "YearsWithCurrManager":    YearsWithCurrManager,
    }

    try:
        endpoint_url = MODEL_CONFIG[model_choice]
        response     = requests.post(endpoint_url, json=payload)

        if response.status_code == 200:
            result = response.json()
            risk   = result["attrition_risk"]
            prob   = result["probability"]
            source = result["model_source"]

            st.divider()
            if risk == "High":
                st.error(f"⚠️  Attrition Risk: **{risk}**")
            else:
                st.success(f"✅  Attrition Risk: **{risk}**")

            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Probability", f"{prob:.2%}")
            with col_b:
                st.metric("Model Source", source)

        else:
            st.error(f"API Error {response.status_code}: {response.json().get('detail')}")

    except requests.exceptions.ConnectionError:
        st.error("❌  Cannot connect to API. Make sure FastAPI is running on port 8001.")