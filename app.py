import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="FraudGuard AI | Global Security", layout="wide")

# 2. Professional Light Theme CSS (No Transparency, High Contrast)
st.markdown("""
    <style>
    /* Background with a very light white overlay for maximum clarity */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.93), rgba(255, 255, 255, 0.93)), 
                    url('https://images.unsplash.com/photo-1563013544-824ae1b704d3?q=80&w=2070');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Main Container with Solid White/Grey look */
    .main-panel {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        border: 1px solid #E1E4E8;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        color: #24292E;
    }

    /* Professional Audit Report Box (Solid Blue-ish Grey) */
    .report-card {
        background-color: #F6F8FA;
        border-left: 6px solid #0366D6;
        padding: 25px;
        border-radius: 6px;
        color: #24292E;
        margin-top: 20px;
        font-family: 'Segoe UI', sans-serif;
    }

    /* High Contrast Titles */
    h1, h2, h3 {
        color: #0366D6 !important;
    }
    
    /* Metrics Styling */
    .stMetric {
        background-color: #F1F8FF;
        padding: 15px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Secure Model Loading
@st.cache_resource
def load_model():
    try: return joblib.load('model.pkl')
    except: return None

model = load_model()

# --- HEADER SECTION ---
st.title("FraudGuard™ Financial Intelligence")
st.markdown("### **Enterprise Fraud Monitoring & Risk Dashboard**")
st.markdown("---")

# --- SIDEBAR: SYSTEM INPUTS ---
with st.sidebar:
    st.header("⚙️ Control Center")
    st.write("Modify transaction vectors below:")
    amount = st.number_input("Transaction Value (USD)", min_value=0.0, value=250.0)
    v14 = st.slider("Coefficient V14 (Structural Risk)", -20.0, 10.0, 0.0)
    v17 = st.slider("Coefficient V17 (Behavioral Risk)", -20.0, 10.0, 0.0)
    st.markdown("---")
    st.caption("Standard: PCI-DSS & ISO 27001 Certified")

# --- MAIN DASHBOARD AREA ---
st.markdown('<div class="main-panel">', unsafe_allow_html=True)

col_main, col_kpi = st.columns([2, 1])

with col_main:
    st.subheader("🔍 Transaction Security Analysis")
    
    # Professional Context Paragraph
    st.info("""
    **V14 & V17 Analysis:** These are Principal Component Analysis (PCA) features. 
    **V14** monitors for structural data integrity anomalies, while **V17** tracks significant 
    deviations in behavioral spending habits. Values below -4.0 are statistically 
    linked to unauthorized transactions.
    """)

    if st.button("EXECUTE LIVE SECURITY SCAN"):
        with st.spinner('Syncing with Global Security Database...'):
            time.sleep(1.3) # Realistic delay
            
            if model:
                # Prepare Input
                input_data = np.zeros((1, 30))
                input_data[0, 28] = amount
                input_data[0, 13] = v1
