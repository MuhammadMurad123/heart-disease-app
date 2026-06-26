import streamlit as st
import pandas as pd

# ایپ کی سیٹنگ
st.set_page_config(page_title="Heart Health Checker", page_icon="❤️", layout="centered")

# --- Custom CSS برائے جدید اور پروفیشنل میڈیکل لُک ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); }
    h1 { color: #1e3799; text-align: center; font-weight: 800; padding-bottom: 20px; }
    .stButton > button { 
        background: linear-gradient(90deg, #0097e6, #273c75); 
        color: white; border-radius: 15px; font-weight: bold; 
        width: 100%; border: none; padding: 12px; transition: 0.3s;
    }
    .stButton > button:hover { transform: scale(1.02); }
    </style>
""", unsafe_allow_html=True)

# زبان کا انتخاب
lang = st.sidebar.selectbox("🌐 Select Language / زبان منتخب کریں", ["English", "Urdu"])

# ٹیکسٹ ڈیٹا
if lang == "Urdu":
    title = "❤️ ہارٹ ہیلتھ چیکر"
    tab1_name, tab2_name = "پریڈکشن (Predict)", "بلک ڈیٹا (CSV)"
    labels = {"gender": "👤 جنس", "age": "👴 عمر (سال)", "bp": "🩸 بلڈ پریشر (mmHg)", "chol": "🧪 کولیسٹرول (mg/dl)", "mhr": "💓 دل کی دھڑکن", "eia": "⚠️ ورزش پر سینے میں درد"}
    btn_txt, success_txt = "دل کی صحت چیک کریں", "مبارک ہو! آپ کی دل کی صحت نارمل ہے۔"
    error_txt, risk_txt = "احتیاط ضروری ہے!", "درج ذیل علامات خطرے کا باعث ہو سکتی ہیں:"
    opt_male, opt_female = "مرد (Male)", "عورت (Female)"
    opt_yes, opt_no = "جی ہاں", "نہیں"
else:
    title = "❤️ Heart Health Checker"
    tab1_name, tab2_name = "Predict", "Bulk Data (CSV)"
    labels = {"gender": "👤 Gender", "age": "👴 Age (Years)", "bp": "🩸 Blood Pressure (mmHg)", "chol": "🧪 Cholesterol (mg/dl)", "mhr": "💓 Max Heart Rate", "eia": "⚠️ Exercise Induced Angina?"}
    btn_txt, success_txt = "Check Heart Health", "Congratulations! Your heart health is normal."
    error_txt, risk_txt = "Caution Required!", "The following symptoms may be a health risk:"
    opt_male, opt_female = "Male", "Female"
    opt_yes, opt_no = "Yes", "No"

st.title(title)
tab1, tab2 = st.tabs([tab1_name, tab2_name])

with tab1:
    # جینڈر کا انتخاب
    gender = st.radio(labels["gender"], [opt_male, opt_female], horizontal=True)
    
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input(labels["age"], 0, 100, 30)
        rbp = st.number_input(labels["bp"], 0, 250, 120)
    with col2:
        mhr = st.number_input(labels["mhr"], 50, 220, 150)
        chol = st.number_input(labels["chol"], 0, 500, 200)
    
    eia = st.selectbox(labels["eia"], [opt_no, opt_yes])

    if st.button(btn_txt):
        risks = []
        
        # جینڈر کی بنیاد پر طبی رینج کا تعین
        if gender == opt_male:
            if rbp > 135: risks.append("High Blood Pressure (Male > 135)")
            if chol > 220: risks.append("High Cholesterol (Male > 220)")
        else: # Female
            if rbp > 125: risks.append("High Blood Pressure (Female > 125)")
            if chol > 210: risks.append("High Cholesterol (Female > 210)")

        # مشترکہ رینج
        if mhr < 100: risks.append("Low Heart Rate")
        if eia == opt_yes: risks.append("Chest pain during exercise")

        if not risks:
            st.success(success_txt)
        else:
            st.error(error_txt)
            st.write(risk_txt)
            for r in risks: st.write(f"⚠️ {r}")

with tab2:
    st.info("Upload your medical report CSV to get bulk analysis.")
    uploaded_file = st.file_uploader("📂 Select CSV File", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)
