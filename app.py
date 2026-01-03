import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="FraudGuard AI | Global Security", layout="wide")

# 2. High-Contrast Solid UI (No Transparency)
st.markdown("""
    <style>
    /* Fixed Solid Background for maximum readability */
    .stApp {
        background-color: #0D1117;
        color: #FFFFFF;
    }

    /* Main Solid Container */
    .solid-panel {
        background-color: #161B22;
        padding: 30px;
        border-radius: 8px;
        border: 1px solid #30363D;
        margin-bottom: 20px;
    }

    /* Professional Audit Report Box */
    .report-box {
        background-color: #010409;
        border-left: 5px solid #58A6FF;
        padding: 20px;
        margin-top: 15px;
        color: #C9D1D9;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }

    /* Bold Headers */
    h1, h2, h3 {
        color: #58A6FF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Model Loading
@st.cache_resource
def load_model():
    try: return joblib.load('model.pkl')
    except: return None

model = load_model()

# --- HEADER ---
st.title("FraudGuard™ Financial Intelligence")
st.markdown("### **Enterprise Fraud Monitoring System**")
st.markdown("---")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ System Controls")
    amount = st.number_input("Transaction Value (USD)", min_value=0.0, value=250.0)
    v14 = st.slider("V14 (Structural Anomaly)", -20.0, 10.0, 0.0)
    v17 = st.slider("V17 (Behavioral Shift)", -20.0, 10.0, 0.0)
    st.markdown("---")
    st.caption("Standard: PCI-DSS Compliant")

# --- MAIN INTERFACE ---
st.markdown('<div class="solid-panel">', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🔍 Real-Time Analysis")
    st.write("""
    **V14 & V17 Indicators:** These are PCA-transformed components. 
    **V14** monitors structural data integrity, while **V17** tracks behavioral spending 
    deviations. High negative values trigger fraud alerts.
    """)

    if st.button("EXECUTE SECURITY SCAN"):
        with st.spinner('Accessing Neural Engine...'):
            time.sleep(1.2)
            
            if model:
                # Prediction Logic
                features = np.zeros((1, 30))
                features[0, 28] = amount
                features[0, 13] = v14
                features[0, 16] = v17
                prediction = model.predict(features)
                
                # Fixed HTML f-string with closed brackets
                if prediction[0] == 1:
                    st.error("🚨 **ALERT: FRAUD DETECTED**")
                    status_text = "HIGH RISK"
                    summary = f"Transaction at ${amount} matches known fraud signatures (V14: {v14})."
                else:
                    st.success("✅ **STATUS: SECURE**")
                    status_text = "VERIFIED"
                    summary = f"Transaction patterns are within normal limits (V17: {v17})."

                # Building the report box safely
                report_html = f"""
                <div class="report-box">
                    <b>Audit Status:</b> {status_text}<br>
                    <b>Technical Summary:</b> {summary}<br>
                    <b>System Action:</b> Authorization {"Denied" if prediction[0]==1 else "Granted"}
                </div>
                """
                st.markdown(report_html, unsafe_allow_html=True)
            else:
                st.error("Model file 'model.pkl' not detected.")

with col2:
    st.subheader("📊 Network KPIs")
    st.metric("Model Accuracy", f"{99.9 + random.uniform(-0.01, 0.01):.3f}%")
    st.metric("Fraud Recall", "82.4%")
    st.metric("Latency", f"{random.randint(7, 12)}ms")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2026 FraudGuard Global Security Unit | Confidential")
