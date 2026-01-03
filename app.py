import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import random

# 1. Page Configuration
st.set_page_config(page_title="FraudGuard AI | Global Security", layout="wide")

# 2. Universal Visibility & Forced Light Sidebar CSS
st.markdown("""
    <style>
    /* Force Sidebar to STAY in Light Theme regardless of system settings */
    [data-testid="stSidebar"] {
        background-color: #F8F9FA !important;
        color: #000000 !important;
    }
    
    /* TARGETED FIX: Sidebar Arrow Icon (>>) Red Color */
    [data-testid="stSidebarCollapseButton"] svg {
        fill: #FF0000 !important;
    }
    
    /* Force Sidebar labels and text to Black for readability */
    [data-testid="stSidebar"] .stMarkdown p, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] h2 {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* Background Clarity */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.3)), 
                    url('https://images.unsplash.com/photo-1563013544-824ae1b704d3?q=80&w=2070');
        background-size: cover;
        background-attachment: fixed;
    }

    /* Main Content Container */
    .solid-container {
        background-color: #FFFFFF !important;
        padding: 35px;
        border-radius: 15px;
        border: 2px solid #000000;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    /* Security Intelligence Feed Box */
    .intel-box {
        background-color: #F8F9FA;
        border: 2px solid #000000;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 25px;
        color: #000000 !important;
    }

    /* Force Button Visibility: Black Background / White Text */
    div.stButton > button {
        background-color: #000000 !important;
        color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        font-weight: 700 !important;
        width: 100%;
        height: 3.5em;
    }

    /* High Contrast Text for Main Body */
    h1, h2, h3, h4, p, span, div, [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    /* Report Card Style */
    .report-card {
        background-color: #000000 !important;
        border-left: 10px solid #28a745;
        padding: 25px;
        border-radius: 8px;
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
    st.write("Real-time transaction adjustments.")
    amount = st.number_input("Transaction Value (USD)", min_value=0.0, value=250.0)
    v14 = st.slider("Coefficient V14 (Structural)", -20.0, 10.0, 0.0)
    v17 = st.slider("Coefficient V17 (Behavioral)", -20.0, 10.0, 0.0)
    st.markdown("---")
    st.caption("Standard: PCI-DSS Compliant")

# --- MAIN DASHBOARD ---
st.markdown('<div class="solid-container">', unsafe_allow_html=True)

# THE INFORMATIVE BOX: Security Intelligence Feed
st.markdown(f"""
<div class="intel-box">
    <h4 style="margin-top:0;">🛡️ Security Intelligence Feed</h4>
    <p style="font-size: 1rem; line-height: 1.5;">
    <b>System Monitor:</b> All protocols operational. The neural network is cross-referencing global pattern clusters
