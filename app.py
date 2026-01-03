import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="FraudGuard AI | Global Security", layout="wide")

# 2. High-Contrast Solid UI CSS
st.markdown("""
    <style>
    /* Background image with a very dark solid overlay */
    .stApp {
        background-color: #0E1117;
        background-image: linear-gradient(rgba(0,0,0,0.9), rgba(0,0,0,0.9)), 
                          url('https://images.unsplash.com/photo-1563013544-824ae1b704d3?q=80&w=2070');
        background-size: cover;
    }

    /* Solid Main Container (No Transparency) */
    .solid-panel {
        background-color: #161B22; /* Solid Dark Grey */
        padding: 35px;
        border-radius: 10px;
        border: 2px solid #30363D;
        color: #FFFFFF;
        margin-bottom: 25px;
    }

    /* High Visibility Report Box */
    .report-card {
        background-color: #0D1117; /* Solid Black */
        border-left: 6px solid #58A6FF;
        padding: 25px;
        border-radius: 5px;
        color: #C9D1D9;
        margin-top: 20px;
        font-size: 1.1rem;
        line-height: 1.6;
    }

    /* Headings */
    h1, h2, h3 {
        color: #58A6FF !important;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }

    /* Sidebar text fix */
    .css-1d391kg {
        background-color: #0D1117 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Model Loading
@st.cache_resource
def load_model():
    try: return joblib.load('model.pkl')
    except: return None

model = load_model()

# --- HEADER SECTION ---
st.title("FraudGuard™ Financial Intelligence")
st.markdown("### **Enterprise Risk Analysis Dashboard**")
st.markdown("---")

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("🔍 Input Parameters")
    st.write("Modify the data vector below:")
    amount = st.number_input("Transaction Value (USD)", min_value=0.0, value=250.0)
    v14 = st.slider("Coefficient V14 (Structural)", -20.0, 10.0, 0.0)
    v17 = st.slider("Coefficient V17 (Behavioral)", -20.0, 10.0, 0.0)
    st.markdown("---")
    st.caption("Compliance: PCI-DSS & ISO 27001")

# --- MAIN DASHBOARD (SOLID PANEL) ---
st.markdown('<div class="solid-panel">', unsafe_allow_html=True)

col_main, col_metrics = st.columns([2, 1])

with col_main:
    st.subheader("Automated Fraud Audit")
    
    # Technical Guidance Paragraph
    st.write("""
    **V14 & V17 Contextual Analysis:** These are Principal Component Analysis (PCA) vectors. 
    **V14** detects structural anomalies in the transaction metadata, while **V17** identifies 
    deviations in established user spending behavior. Values moving significantly 
    into the negative spectrum indicate a heightened risk of fraudulent activity.
    """)

    if st.button("EXECUTE SECURITY SCAN"):
        with st.spinner('Accessing Neural Engine...'):
            time.sleep(1.5)
            
            if model:
                # Prepare Data
                input_data = np.zeros((1, 30))
                input_data[0, 28] = amount
                input_data[0, 13] = v14
                input_data[0, 16] = v17
                prediction = model.predict(input_data)
                
                # Report Logic
                if prediction[0] == 1:
                    st.error("🚨 **RISK ALERT: UNAUTHORIZED PATTERN**")
                    status = "HIGH RISK"
                    summary = f"The transaction at ${amount} displays a structural signature consistent with fraud (V14: {v14})."
                    action = "Immediate account lock and manual review recommended."
                else:
                    st.success("✅ **STATUS: TRANSACTION SECURE**")
                    status = "LEGITIMATE"
                    summary = f"Transaction behavior is within normal standard deviations (V17: {v17})."
                    action = "Automated authorization granted for settlement."

                # --- THE AUDIT REPORT BOX ---
                st.markdown(f"""
                <div class="report-card">
                <b>Audit Status:</b> {status
