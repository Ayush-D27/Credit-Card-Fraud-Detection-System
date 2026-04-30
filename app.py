import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("C:/Users/ayush/OneDrive/Documents/ML_project/Credit Card Fraud Detection System/model.pkl")

# Page config
st.set_page_config(page_title="Credit Card Fraud Detection System", page_icon="💳", layout="centered")

# ---------- MODERN CSS ----------
st.markdown("""
<style>
/* Background Gradient */
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

/* Center container */
.main {
    background: transparent;
}

/* Title */
.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    color: white;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #e0e0e0;
    margin-bottom: 30px;
}

/* Glass Card */
.card {
    background: rgba(255,255,255,0.1);
    padding: 25px;
    border-radius: 16px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #ff6a00, #ee0979);
    color: white;
    border-radius: 14px;
    height: 50px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

/* Input labels */
label {
    color: white !important;
    font-weight: 500;
}

/* Footer */
.footer {
    text-align: center;
    color: #cccccc;
    margin-top: 20px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="title">💳 Credit Card Fraud Detection</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart AI-based transaction analysis</div>', unsafe_allow_html=True)

# ---------- INPUT CARD ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📊 Transaction Details")

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input("💰 Amount", min_value=0.0)
    v1 = st.number_input("🔢 V1")

with col2:
    time = st.number_input("⏱ Time", min_value=0.0)
    v2 = st.number_input("🔢 V2")

v3 = st.number_input("🔢 V3")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- BUTTON ----------
if st.button("🚀 Analyze Transaction"):

    # Create full 30 feature input
    input_data = [0]*30
    input_data[0] = time
    input_data[1] = amount
    input_data[2] = v1
    input_data[3] = v2
    input_data[4] = v3

    input_data = np.array([input_data])

    prediction = model.predict(input_data)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if prediction[0] == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown('<div class="footer">✨ Built using Machine Learning & Streamlit</div>', unsafe_allow_html=True)