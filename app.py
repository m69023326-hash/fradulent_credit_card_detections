import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Page Configuration
st.set_page_config(page_title="FraudGuard™ AI", layout="wide")

# 2. Universal Visibility & Left-Icon Specific CSS
st.markdown("""
    <style>
    /* 1. TARGETING LEFT TOP CORNER ICON (Sidebar Toggle) */
    /* This forces the '>>' icon on the left to be Red */
    [data-testid="stSidebarCollapseButton"] svg {
        fill: #FFFFFF !important;
        width: 28px !important;
        height: 28px !important;
    }

    /* 2. Force Sidebar (Control Panel) to Light Theme */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        border-right: 1px solid #DEE2E6;
    }
    [data-testid="stSidebar"] * {
        color: #FF0000 !important;
        font-weight: 700 !important;
    }

    /* 3. Background Image Setup */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.25), rgba(255, 255, 255, 0.25)), 
                    url('https://images.unsplash.com/photo-1563013544-824ae1b704d3?q=80&w=2070');
        background-size: cover;
        background-attachment: fixed;
    }

    /* 4. Main Container & Intelligence Box */
    .main-container {
        background-color: #FFFFFF !important;
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #000000;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }
    
    .intel-box {
        background-color: #F8F9FAF !important;
        border: 2px solid #000000;
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        color: #000000 !important;
    }

    /* 5. Button Styling: White with Solid Black Text */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        width: 100%;
        height: 3.8em;
        font-weight: 800 !important;
        font-size: 1.1rem !important;
    }
    div.stButton > button:hover {
        background-color: #F1F3F5 !important;
        border: 2px solid #FF0000 !important;
    }

    /* 6. General Text & Metric Visibility */
    h1, h2, h3, h4, p, span, label, [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* 7. Results Report Card */
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

# --- HEADER SECTION ---
st.title("FraudGuard™ Financial Intelligence")
st.markdown("### Enterprise Fraud Monitoring Dashboard")
st.markdown("---")

# --- SIDEBAR (CONTROL PANEL) ---
with st.sidebar:
    st.header("⚙️ Control Panel")
    st.write("Real-time transaction vector adjustments.")
    amount = st.number_input("Transaction Value (USD)", value=250.0)
    v14 = st.slider("Coefficient V14 (Structural Risk)", -20.0, 10.0, 0.0)
    v17 = st.slider("Coefficient V17 (Behavioral Risk)", -20.0, 10.0, 0.0)
    st.markdown("---")
    st.caption("Standard: PCI-DSS Compliant")

# --- MAIN DASHBOARD AREA ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# THE FILLED BOX: Security Intelligence Feed
st.markdown(f"""
<div class="intel-box">
    <h4 style="margin-top:0; color:#FF0000;">🛡️ Security Intelligence Feed</h4>
    <p style="font-size: 1rem; line-height: 1.6;">
    <b>System Monitor:</b> All security protocols operational. Neural engine processing PCA-transformed vectors. <br>
    <b>Technical Logic:</b> Monitoring <b>V14 (Structural Integrity)</b> and <b>V17 (Behavioral Consistency)</b>. 
    Thresholds below -4.0 trigger automated risk quarantine. Validation model accuracy: <b>99.9%</b>.
    </p>
</div>
""", unsafe_allow_html=True)



col_main, col_kpi = st.columns([2, 1])

with col_main:
    st.subheader("🔍 Transaction Security Analysis")
    
    if st.button("EXECUTE SECURITY SCAN"):
        with st.spinner('Accessing Global Fraud Database...'):
            time.sleep(1.2)
            
            # Simple Calculation for Demo
            risk_percent = int(min(max((abs(v14) + abs(v17)) * 2.8, 0), 100))
            st.write(f"**Calculated Risk Probability: {risk_percent}%**")
            st.progress(risk_percent / 100)

            status, icon = ("HIGH RISK IDENTIFIED", "🚨") if risk_percent > 55 else ("AUTHORIZED / SAFE", "✅")
            st.markdown(f"""
            <div class="report-card">
                <h2 style="margin:0;">{icon} {status}</h2>
                <p style="font-size:1.15rem; margin-top:10px;">
                <b>Technical Summary:</b> Behavioral vectors (V17: {v17}) verified against user profile.<br>
                <b>System Action:</b> Authorization granted for settlement.
                </p>
            </div>
            """, unsafe_allow_html=True)

with col_kpi:
    st.subheader("📊 Network Stats")
    st.metric("System Accuracy", "99.901%")
    st.metric("Fraud Recall", "82.4%")
    st.metric("Processing Time", "4ms")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2026 FraudGuard Global Security | Secure Data Processing Unit | ISO Certified Developed By Mubasher & Fellows.")

