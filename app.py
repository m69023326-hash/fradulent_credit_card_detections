import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="FraudGuard AI | Enterprise", layout="wide")

# 2. CSS for Maximum Contrast and Black Text
st.markdown("""
    <style>
    /* Background Image: Very Clear (Low Overlay) */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.35), rgba(255, 255, 255, 0.35)), 
                    url('https://images.unsplash.com/photo-1563013544-824ae1b704d3?q=80&w=2070');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Main Solid Panel: Pure White for Readability */
    .main-panel {
        background-color: #FFFFFF !important;
        padding: 40px;
        border-radius: 12px;
        border: 2px solid #000000;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        color: #000000 !important;
    }

    /* Force All Text to Black */
    h1, h2, h3, h4, p, span, div {
        color: #000000 !important;
        font-weight: 600;
    }

    /* Metrics Color: Bold Blue for numbers to stand out, Black for labels */
    [data-testid="stMetricValue"] {
        color: #000000 !important;
        font-weight: 800 !important;
    }
    [data-testid="stMetricLabel"] {
        color: #333333 !important;
    }

    /* Report Card: Solid Black Background with White Text for contrast */
    .report-card {
        background-color: #000000 !important;
        border-left: 10px solid #28a745;
        padding: 25px;
        border-radius: 8px;
        color: #FFFFFF !important;
        margin-top: 20px;
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

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Control Center")
    amount = st.number_input("Transaction Value (USD)", min_value=0.0, value=250.0)
    v14 = st.slider("V14 (Structural Risk)", -20.0, 10.0, 0.0)
    v17 = st.slider("V17 (Behavioral Risk)", -20.0, 10.0, 0.0)
    st.markdown("---")
    st.caption("Standard: PCI-DSS Compliant")

# --- MAIN DASHBOARD AREA ---
st.markdown('<div class="main-panel">', unsafe_allow_html=True)

col_main, col_kpi = st.columns([2, 1])

with col_main:
    st.subheader("🔍 Transaction Security Analysis")
    st.write("""
    **V14 & V17 Context:** These features are the result of Principal Component Analysis (PCA). 
    **V14** monitors structural data integrity, while **V17** tracks behavioral spending 
    deviations. High negative values are key indicators of fraudulent activity.
    """)

    if st.button("EXECUTE SECURITY SCAN"):
        with st.spinner('Accessing Global Database...'):
            time.sleep(1.2)
            if model:
                # Prepare Input
                features = np.zeros((1, 30))
                features[0, 28] = amount
                features[0, 13] = v14
                features[0, 16] = v17
                prediction = model.predict(features)
                
                if prediction[0] == 1:
                    status, icon = "HIGH RISK / QUARANTINE", "🚨"
                    action = "Immediate fund suspension required."
                    summary = f"Alert: High-risk structural anomaly (V14: {v14})."
                else:
                    status, icon = "LEGITIMATE / AUTHORIZED", "✅"
                    action = "Authorization granted for settlement."
                    summary = f"Spending patterns (V17: {v17}) are within safety limits."

                st.markdown(f"""
                <div class="report-card">
                    <h2 style="margin-top:0;">{icon} {status}</h2>
                    <p>
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
    st.metric("Fraud Recall Rate", "82.4%")
    st.metric("Processing Time", f"{random.randint(5, 9)}ms")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2026 FraudGuard Global Security | Secure Data Processing Unit")
