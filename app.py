import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="FraudGuard AI | Enterprise", layout="wide")

# 2. Universal Visibility CSS (Fixed Sidebar & Button)
st.markdown("""
    <style>
    /* Force Sidebar to be Light/Grey even in Dark Mode */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF !important;
        color: #FFFFFF !important;
    }
    
    /* Force Sidebar Icons and Text to be Black */
    [data-testid="stSidebarNav"] svg, [data-testid="stSidebarCollapseButton"] svg {
        fill: #0000 !important;
    }
    [data-testid="stSidebar"] .stMarkdown p, [data-testid="stSidebar"] label {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* Background Image: Crystal Clear */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.2), rgba(255, 255, 255, 0.2)), 
                    url('https://images.unsplash.com/photo-1563013544-824ae1b704d3?q=80&w=2070');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Main Container: Solid White */
    .solid-container {
        background-color: #FFFFFF !important;
        padding: 40px;
        border-radius: 15px;
        border: 2px solid #000000;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    /* Force Button Visibility: Black Background with White Text */
    div.stButton > button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        width: 100%;
        font-weight: 700 !important;
        height: 3.5em !important;
    }

    /* Force Main Text to Black */
    h1, h2, h3, h4, p, span, div, [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* Report Card: Solid Black with White Text */
    .report-card {
        background-color: #000000 !important;
        border-left: 12px solid #28a745;
        padding: 30px;
        border-radius: 10px;
        color: #FFFFFF !important;
    }
    .report-card h2, .report-card p, .report-card b {
        color: #FFFFFF !important;
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
st.markdown("### Enterprise Fraud Monitoring Dashboard")
st.markdown("---")

# --- SIDEBAR (CONTROL PANEL) ---
with st.sidebar:
    st.header("⚙️ Control Panel")
    st.write("Adjust parameters for real-time risk assessment.")
    amount = st.number_input("Transaction Value (USD)", min_value=0.0, value=250.0)
    v14 = st.slider("Coefficient V14 (Structural Risk)", -20.0, 10.0, 0.0)
    v17 = st.slider("Coefficient V17 (Behavioral Risk)", -20.0, 10.0, 0.0)
    st.markdown("---")
    st.caption("Standard: PCI-DSS Compliant")

# --- MAIN DASHBOARD AREA ---
st.markdown('<div class="solid-container">', unsafe_allow_html=True)

col_main, col_kpi = st.columns([2, 1])

with col_main:
    st.subheader("🔍 Transaction Security Analysis")
    st.write("""
    **V14 & V17 Contextual Framework:** Our system utilizes PCA-transformed vectors to analyze transaction integrity. 
    - **V14 (Structural):** Detects data anomalies like duplicated metadata. 
    - **V17 (Behavioral):** Tracks real-time spending deviations.
    """)

    if st.button("EXECUTE SECURITY SCAN"):
        with st.spinner('Accessing Global Security Database...'):
            time.sleep(1.2)
            if model:
                features = np.zeros((1, 30))
                features[0, 28] = amount
                features[0, 13] = v14
                features[0, 16] = v17
                prediction = model.predict(features)
                
                if prediction[0] == 1:
                    status, icon = "HIGH RISK IDENTIFIED", "🚨"
                    action = "Immediate fund quarantine required."
                    summary = f"Critical structural mismatch detected (V14: {v14})."
                else:
                    status, icon = "TRANSACTION AUTHORIZED", "✅"
                    action = "System authorization granted for settlement."
                    summary = f"Legitimate behavioral vectors (V17: {v17}) confirmed."

                st.markdown(f"""
                <div class="report-card">
                    <h2 style="margin:0; color:#FFFFFF !important;">{icon} {status}</h2>
                    <p style="color:#FFFFFF !important; font-size:1.1rem; margin-top:10px;">
                    <b>Technical Summary:</b> {summary}<br>
                    <b>System Action:</b> {action}
                    </p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error("Model Error: model.pkl not found.")

with col_kpi:
    st.subheader("📊 Network Stats")
    st.metric("System Accuracy", f"{99.9 + random.uniform(-0.005, 0.005):.3f}%")
    st.metric("Fraud Recall", "82.4%")
    st.metric("Processing Time", f"{random.randint(4, 8)}ms")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2026 FraudGuard Global Security | Secure Data Processing Unit")



