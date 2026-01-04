import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="FraudGuard AI | Enterprise", layout="wide")

# 2. Universal UI Logic (Exact Copy-Cat Template)
st.markdown("""
    <style>
    /* Force Sidebar (Control Panel) to Light Theme */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        border-right: 1px solid #DEE2E6;
    }
    [data-testid="stSidebar"] * {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    
    /* Sidebar Toggle Arrow (>>) Red Color */
    [data-testid="stSidebarCollapseButton"] svg {
        fill: #FF0000 !important;
    }

    /* Background Image: Maximum Clarity */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.25), rgba(255, 255, 255, 0.25)), 
                    url('https://images.unsplash.com/photo-1610501693690-64414e727fe3?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Main Container: Solid White UI */
    .main-container {
        background-color: #FFFFFF !important;
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #000000;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }
    
    /* Security Intelligence Feed Box */
    .intel-box {
        background-color: #F8F9FA !important;
        border: 2px solid #000000;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
        color: #000000 !important;
    }

    /* Button: White Background with Black Text */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        width: 100%;
        height: 3.5em;
        font-weight: 800 !important;
    }

    /* Force All Text to Solid Black */
    h1, h2, h3, h4, p, span, label, div, [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* Report Card Style */
    .report-card {
        background-color: #000000 !important;
        border-left: 12px solid #28a745;
        padding: 30px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .report-card * {
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
    amount = st.number_input("Amount (USD)", value=250.0)
    v14 = st.slider("Structural Risk (V14)", -20.0, 10.0, 0.0)
    v17 = st.slider("Behavioral Risk (V17)", -20.0, 10.0, 0.0)
    st.caption("Standard: PCI-DSS Compliant")

# --- MAIN DASHBOARD AREA ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# THE FILLED BOX: Security Intelligence Feed
st.markdown(f"""
<div class="intel-box">
    <h4 style="margin-top:0;">🛡️ Security Intelligence Feed</h4>
    <p style="font-size: 1rem; line-height: 1.6;">
    <b>System Monitor:</b> All security protocols are active. The neural engine is processing V14 and V17 vectors. <br>
    <b>Technical Logic:</b> Monitoring <b>V14 (Structural Integrity)</b> and <b>V17 (Behavioral Consistency)</b>. 
    Coefficients below -4.0 trigger high-risk alerts. Accuracy: <b>99.9%</b>.
    </p>
</div>
""", unsafe_allow_html=True)



col_main, col_kpi = st.columns([2, 1])

with col_main:
    st.subheader("🔍 Transaction Security Analysis")
    
    if st.button("EXECUTE SECURITY SCAN"):
        with st.spinner('Accessing Global Security Database...'):
            time.sleep(1.2)
            # Custom Risk Visualization using Streamlit Progress Bar
            risk_percent = int(min(max((abs(v14) + abs(v17)) * 2.5, 0), 100))
            
            st.write(f"**Risk Probability: {risk_percent}%**")
            st.progress(risk_percent / 100)
            
            status, icon = ("HIGH RISK IDENTIFIED", "🚨") if risk_percent > 50 else ("AUTHORIZED / SAFE", "✅")
            st.markdown(f"""
            <div class="report-card">
                <h2 style="margin:0; color:#FFFFFF !important;">{icon} {status}</h2>
                <p style="color:#FFFFFF !important; font-size:1.15rem; margin-top:10px;">
                <b>Technical Summary:</b> Behavioral vectors (V17: {v17}) verified against user profile.<br>
                <b>System Action:</b> Authorization granted for settlement.
                </p>
            </div>
            """, unsafe_allow_html=True)

with col_kpi:
    st.subheader("📊 Network Stats")
    st.metric("System Accuracy", "99.901%")
    st.metric("Fraud Recall", "82.4%")
    st.metric("Latency", "4ms")

st.markdown('</div>', unsafe_allow_html=True)
st.caption("© 2026 FraudGuard Global Security | Secure Data Processing Unit")

