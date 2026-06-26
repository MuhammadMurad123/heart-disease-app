import streamlit as st
import pandas as pd

# ایپ کی سیٹنگ
st.set_page_config(page_title="Heart Health Checker", page_icon="❤️", layout="wide")

# --- Custom CSS برائے پروفیشنل میڈیکل لُک ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    h1 { color: #2c3e50; text-align: center; font-family: 'Segoe UI', sans-serif; }
    div.stButton > button { 
        background-color: #27ae60; color: white; border-radius: 8px; 
        font-weight: bold; width: 100%; border: none; padding: 10px;
    }
    .stApp { border-top: 5px solid #27ae60; }
    </style>
""", unsafe_allow_html=True)

# زبان کا انتخاب
lang = st.sidebar.selectbox("Select Language / زبان منتخب کریں", ["English", "Urdu"])

# ٹیکسٹ ڈیٹا
if lang == "Urdu":
    title = "❤️ ہارٹ ہیلتھ چیکر"
    tab1_name, tab2_name = "پریڈکشن (Predict)", "بلک پریڈکشن (CSV)"
    labels = {"age": "عمر (سال)", "bp": "بلڈ پریشر (mmHg)", "chol": "کولیسٹرول (mg/dl)", "mhr": "دل کی دھڑکن", "eia": "ورزش پر سینے میں درد"}
    btn_txt, success_txt = "دل کی صحت چیک کریں", "مبارک ہو! آپ کی دل کی صحت نارمل ہے۔"
    error_txt, risk_txt = "احتیاط ضروری ہے!", "درج ذیل علامات خطرے کا باعث ہو سکتی ہیں:"
    opt_yes, opt_no = "جی ہاں", "نہیں"
else:
    title = "❤️ Heart Health Checker"
    tab1_name, tab2_name = "Predict", "Bulk Predict (CSV)"
    labels = {"age": "Age (Years)", "bp": "Blood Pressure (mmHg)", "chol": "Cholesterol (mg/dl)", "mhr": "Max Heart Rate", "eia": "Exercise Induced Angina?"}
    btn_txt, success_txt = "Check Heart Health", "Congratulations! Your heart health is normal."
    error_txt, risk_txt = "Caution Required!", "The following symptoms may be a health risk:"
    opt_yes, opt_no = "Yes", "No"

st.title(title)
tab1, tab2 = st.tabs([tab1_name, tab2_name])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input(labels["age"], 0, 100, 30)
        rbp = st.number_input(labels["bp"], 0, 250, 120)
        chol = st.number_input(labels["chol"], 0, 500, 200)
    with col2:
        mhr = st.number_input(labels["mhr"], 50, 220, 150)
        eia = st.selectbox(labels["eia"], [opt_no, opt_yes])

    if st.button(btn_txt):
        risks = []
        if rbp > 140: risks.append("High Blood Pressure")
        if chol > 240: risks.append("High Cholesterol")
        if mhr < 100: risks.append("Low Heart Rate")
        if eia == opt_yes: risks.append("Chest pain during exercise")

        if not risks:
            st.success(success_txt)
        else:
            st.error(error_txt)
            st.write(risk_txt)
            for r in risks: st.write(f"⚠️ {r}")

with tab2:
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        if st.button("Process Data"):
            st.write("Results generated.") # یہاں آپ اپنا پروسیسنگ لاجک لگا سکتے ہیں