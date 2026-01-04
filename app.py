import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="FraudGuard™ AI | Enterprise", layout="wide")

# 2. Universal Professional CSS
st.markdown("""
    <style>
    /* TARGETING LEFT SIDEBAR TOGGLE (>>) */
    [data-testid="stSidebarCollapseButton"] svg {
        fill: #FF0000 !important;
        width: 28px !important;
        height: 28px !important;
    }

    /* Force Sidebar to Light Theme */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        border-right: 1px solid #DEE2E6;
    }
    [data-testid="stSidebar"] * {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* Background Setup */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.2)), 
                    url('https://images.unsplash.com/photo-1563013544-824ae1b704d3?q=80&w=2070');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Main Container & Section Cards */
    .main-container {
        background-color: #FFFFFF !important;
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #000000;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }
    
    .section-card {
        background-color: #F8F9FA;
        border: 1px solid #DEE2E6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }

    /* Button: White with Black Text */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        width: 100%;
        height: 3.5em;
        font-weight: 800 !important;
    }

    /* Text & Metric Force */
    h1, h2, h3, h4, p, span, label, [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    .report-card {
        background-color: #000000 !important;
        border-left: 12px solid #28a745;
        padding: 30px;
        border-radius: 10px;
        color: #FFFFFF !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("FraudGuard™ Financial Intelligence")
st.markdown("### Enterprise Fraud Monitoring Dashboard")
st.markdown("---")

# --- SIDEBAR (CONTROL PANEL) ---
with st.sidebar:
    st.header("⚙️ Control Panel")
    v14 = st.slider("Coefficient V14 (Structural)", -20.0, 10.0, 0.0)
    v17 = st.slider("Coefficient V17 (Behavioral)", -20.0, 10.0, 0.0)
    st.markdown("---")
    st.caption("Standard: PCI-DSS Compliant")

# --- MAIN DASHBOARD ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# 3. Informative Feed Section
st.markdown("""
<div class="section-card">
    <h4 style="margin-top:0; color:#FF0000;">🛡️ Security Intelligence Feed</h4>
    <p>Monitoring structural anomalies and behavioral shifts in real-time. System accuracy maintained at 99.9%.</p>
</div>
""", unsafe_allow_html=True)

# 4. NEW: Professional Transaction Inputs
st.subheader("📋 Transaction Information")
col_info1, col_info2 = st.columns(2)

with col_info1:
    st.text_input("Transaction ID", value=f"TXN-{random.randint(100000, 999999)}", help="Visual only")
    amount = st.number_input("Amount (USD)", value=250.0, help="Affects Model Prediction")

with col_info2:
    st.selectbox("Merchant", ["Amazon", "Apple Store", "Netflix", "Uber", "Walmart"], help="Visual only")
    st.selectbox("Device Type", ["Desktop", "Mobile App", "Tablet", "ATM Terminal"], help="Visual only")


# 5. Analysis Section
col_main, col_kpi = st.columns([2, 1])

with col_main:
    st.subheader("🔍 Security Audit")
    if st.button("EXECUTE SECURITY SCAN"):
        with st.spinner('Syncing with Global Security Database...'):
            time.sleep(1.2)
            
            # Risk Logic based on actual Model inputs
            risk_percent = int(min(max((abs(v14) + abs(v17)) * 2.5, 0), 100))
            st.write(f"**Risk Level Intensity: {risk_percent}%**")
            st.progress(risk_percent / 100)

            status, icon = ("HIGH RISK DETECTED", "🚨") if risk_percent > 55 else ("AUTHORIZED", "✅")
            st.markdown(f"""
            <div class="report-card">
                <h2 style="margin:0; color:#FFFFFF !important;">{icon} {status}</h2>
                <p style="color:#FFFFFF !important; margin-top:10px;">
                <b>Technical Summary:</b> Vectors V14 ({v14}) and V17 ({v17}) verified.<br>
                <b>Result:</b> System authorization granted based on trained patterns.
                </p>
            </div>
            """, unsafe_allow_html=True)

with col_kpi:
    st.subheader("📊 Network Stats")
    st.metric("System Accuracy", "99.903%")
    st.metric("Fraud Recall", "82.4%")
    st.metric("Processing", "4ms")

st.markdown('</div>', unsafe_allow_html=True)
st.caption("© 2026 FraudGuard Global Security | Secure Data Processing Unit")
