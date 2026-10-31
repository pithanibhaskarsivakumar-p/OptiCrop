"""
OptiCrop - Intelligent Crop Recommendation Web Application
Built with Streamlit and Scikit-Learn
"""

import os
import json
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

from src.predict import CropRecommender, PARAM_CONSTRAINTS
from src.crop_info import CROP_DETAILS, get_crop_metadata

# Page configuration
st.set_page_config(
    page_title="OptiCrop – Intelligent Crop Recommendation",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1e4620;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4b6354;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border: 1px solid #86efac;
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
    .crop-hero {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 100%);
        border: 2px solid #34d399;
        border-radius: 16px;
        padding: 1.8rem;
        text-align: center;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .crop-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #065f46;
        margin-top: 0.5rem;
    }
    .scientific-name {
        font-style: italic;
        color: #047857;
        font-size: 1.1rem;
        margin-bottom: 0.8rem;
    }
    .info-box {
        background: #ffffff;
        border-radius: 10px;
        border-left: 4px solid #10b981;
        padding: 1rem;
        margin-top: 0.8rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0px 0px;
        padding: 10px 16px;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_engine():
    return CropRecommender("models/crop_rf_model.joblib")

recommender = load_engine()

# Presets for instant demonstration
PRESETS = {
    "-- Custom Input --": None,
    "🌾 Rice (High Rainfall, Subtropical, High N)": {
        "N": 90.0, "P": 42.0, "K": 43.0, "temperature": 21.0, "humidity": 82.0, "ph": 6.5, "rainfall": 202.0
    },
    "☕ Coffee (Highland, Humid, Moderate P & K)": {
        "N": 100.0, "P": 20.0, "K": 30.0, "temperature": 25.0, "humidity": 60.0, "ph": 6.7, "rainfall": 160.0
    },
    "🍎 Apple (Temperate, Chilly, High P & K)": {
        "N": 20.0, "P": 130.0, "K": 200.0, "temperature": 22.0, "humidity": 92.0, "ph": 6.0, "rainfall": 110.0
    },
    "🍉 Watermelon (Warm, Sandy, Balanced NPK)": {
        "N": 100.0, "P": 18.0, "K": 50.0, "temperature": 26.0, "humidity": 85.0, "ph": 6.5, "rainfall": 50.0
    },
    "☁️ Cotton (Black Soil, High N, Moderate Rain)": {
        "N": 120.0, "P": 45.0, "K": 20.0, "temperature": 24.0, "humidity": 80.0, "ph": 6.9, "rainfall": 80.0
    },
    "🧆 Chickpea (Rabi / Legume, Low Moisture & N)": {
        "N": 40.0, "P": 68.0, "K": 79.0, "temperature": 18.5, "humidity": 17.0, "ph": 7.3, "rainfall": 78.0
    }
}

# Sidebar
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1500937386664-56d1dfef3854?auto=format&fit=crop&w=400&q=80", use_container_width=True)
    st.markdown("### 🌾 OptiCrop Advisory")
    st.markdown(
        "**OptiCrop** is an AI-powered agricultural recommendation platform that helps farmers and agronomists "
        "select the most productive crop based on precision soil chemistry and climate analytics."
    )
    
    st.markdown("---")
    st.markdown("#### ⚡ Quick Presets")
    selected_preset_name = st.selectbox("Load Preconfigured Scenario:", list(PRESETS.keys()))
    
    st.markdown("---")
    st.markdown("#### 📊 Model Vital Signs")
    st.metric("Test Set Accuracy", f"{recommender.metrics.get('test_accuracy', 0.9955) * 100:.2f}%")
    st.metric("5-Fold Cross Validation", f"{recommender.metrics.get('cv_accuracy_mean', 0.9955) * 100:.2f}%")
    st.metric("Total Supported Crops", f"{len(recommender.classes)} varieties")

# Tabs
tab_recommend, tab_insights, tab_batch, tab_about = st.tabs([
    "🌱 Crop Recommendation",
    "📈 Model & Feature Insights",
    "📑 Batch CSV Prediction",
    "📘 About & Agronomy Guide"
])

preset_data = PRESETS[selected_preset_name]

# TAB 1: RECOMMENDATION
with tab_recommend:
    st.markdown('<div class="main-header">OptiCrop – Intelligent Crop Recommendation</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">Input soil nutrient parameters and environmental climate factors to receive machine learning crop recommendations.</div>',
        unsafe_allow_html=True
    )
    
    # Input columns
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        st.markdown("##### 🧪 Soil Macronutrients (NPK)")
        
        n_val = float(preset_data["N"]) if preset_data else 90.0
        p_val = float(preset_data["P"]) if preset_data else 42.0
        k_val = float(preset_data["K"]) if preset_data else 43.0
        ph_val = float(preset_data["ph"]) if preset_data else 6.5
        
        n_input = st.slider("Nitrogen (N) in soil (kg/ha)", min_value=0.0, max_value=140.0, value=n_val, step=1.0, help="Essential for leaf growth and lush green vegetation")
        p_input = st.slider("Phosphorus (P) in soil (kg/ha)", min_value=5.0, max_value=145.0, value=p_val, step=1.0, help="Essential for root development, seed, and flower formation")
        k_input = st.slider("Potassium (K) in soil (kg/ha)", min_value=5.0, max_value=205.0, value=k_val, step=1.0, help="Enhances drought resistance, vigor, and fruit quality")
        ph_input = st.slider("Soil pH Level", min_value=3.5, max_value=9.5, value=ph_val, step=0.1, help="Soil acidity or alkalinity (7.0 is neutral)")

    with col_input2:
        st.markdown("##### ⛅ Environmental & Climate Metrics")
        
        temp_val = float(preset_data["temperature"]) if preset_data else 21.0
        hum_val = float(preset_data["humidity"]) if preset_data else 82.0
        rain_val = float(preset_data["rainfall"]) if preset_data else 202.0
        
        temp_input = st.slider("Ambient Temperature (°C)", min_value=5.0, max_value=50.0, value=temp_val, step=0.5, help="Average daytime/growing season temperature")
        hum_input = st.slider("Relative Humidity (%)", min_value=10.0, max_value=100.0, value=hum_val, step=1.0, help="Moisture saturation level in the atmosphere")
        rain_input = st.slider("Seasonal Rainfall (mm)", min_value=10.0, max_value=350.0, value=rain_val, step=1.0, help="Total or seasonal precipitation amount")

    st.markdown("<br>", unsafe_allow_html=True)
    
    predict_clicked = st.button("🔍 Recommend Best-Suited Crop", type="primary", use_container_width=True)
    
    # Process Recommendation
    res = recommender.recommend(
        nitrogen=n_input,
        phosphorus=p_input,
        potassium=k_input,
        temperature=temp_input,
        humidity=hum_input,
        ph=ph_input,
        rainfall=rain_input,
        top_k=3
    )
    
    st.markdown("---")
    
    res_col1, res_col2 = st.columns([1.1, 0.9])
    
    with res_col1:
        primary = res["primary_recommendation"]
        meta = res["primary_metadata"]
        conf = res["primary_confidence_percent"]
        icon = meta.get("icon", "🌱")
        
        st.markdown(f"""
        <div class="crop-hero">
            <span style="font-size: 4rem;">{icon}</span>
            <div class="crop-title">{primary.upper()}</div>
            <div class="scientific-name">{meta.get('common_name', primary.title())} ({meta.get('scientific_name', '')})</div>
            <span style="background-color: #059669; color: white; padding: 4px 14px; border-radius: 20px; font-weight: 600; font-size: 0.9rem;">
                Confidence: {conf:.1f}%
            </span>
            <div style="margin-top: 10px; font-weight: 500; color: #047857;">
                Category: {meta.get('category', 'Field Crop')}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="info-box">
            <b>🌱 Sowing & Harvest Season:</b> {meta.get('growing_season', 'Standard Season')}<br>
            <b>💧 Water Requirement:</b> {meta.get('water_requirement', 'Moderate')}<br>
            <b>🏜️ Optimum Soil Type:</b> {meta.get('soil_type', 'Loam / Alluvial')}<br>
            <b>💡 Agronomic Advice:</b> {meta.get('agronomic_advice', 'Follow regional best management practices.')}
        </div>
        """, unsafe_allow_html=True)

    with res_col2:
        st.markdown("#### 🏆 Top-3 Recommendation Probabilities")
        
        top_recs = res["top_recommendations"]
        rec_data = []
        for r in top_recs:
            rec_data.append({
                "Crop": f"{r['metadata'].get('icon', '🌱')} {r['crop'].title()}",
                "Probability (%)": r["confidence_percent"]
            })
        rec_df = pd.DataFrame(rec_data)
        
        # Display bar chart
        st.bar_chart(rec_df.set_index("Crop"), color="#059669")
        
        st.markdown("##### Candidate Crop Breakdown")
        for r in top_recs:
            st.write(f"**Rank {r['rank']}: {r['metadata'].get('icon', '🌱')} {r['crop'].title()}** — `{r['confidence_percent']:.1f}% confidence`")
            st.caption(f"Category: {r['metadata'].get('category', 'Crop')} | Season: {r['metadata'].get('growing_season', 'General')}")
            
    # Parameter suitability breakdown
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("🔬 View Detailed Soil & Climate Parameter Suitability Analysis", expanded=True):
        st.write(f"How your input values compare against the statistical norms for **{primary.title()}**:")
        
        suit_data = []
        for feat, details in res["primary_suitability"].items():
            if "ideal_mean" in details:
                suit_data.append({
                    "Parameter": PARAM_CONSTRAINTS[feat]["desc"],
                    "Input Value": details["input_value"],
                    "Crop Ideal Mean": details["ideal_mean"],
                    "Ideal Range": f"{details['ideal_range'][0]} - {details['ideal_range'][1]}",
                    "Status": details["status"],
                    "Agronomic Assessment": details["comment"]
                })
        st.dataframe(pd.DataFrame(suit_data), use_container_width=True)

# TAB 2: MODEL & FEATURE INSIGHTS
with tab_insights:
    st.markdown("### 📊 OptiCrop Machine Learning Architecture & Insights")
    st.write(
        "The model is a **Random Forest Classifier** trained on the Kaggle Crop Recommendation dataset "
        "comprising 2,200 empirical field records across 22 distinct agricultural crops."
    )
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    col_m1.metric("Overall Accuracy", f"{recommender.metrics.get('test_accuracy', 0.9955) * 100:.2f}%")
    col_m2.metric("Weighted F1-Score", f"{recommender.metrics.get('test_f1', 0.9955):.4f}")
    col_m3.metric("5-Fold CV Score", f"{recommender.metrics.get('cv_accuracy_mean', 0.9955) * 100:.2f}%")
    col_m4.metric("Estimators", "100 Decision Trees")
    
    st.markdown("---")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("#### 🌳 Feature Importance (Gini Impurity Metric)")
        st.caption("How much each environmental and soil parameter influences crop classification:")
        
        fi = recommender.feature_importances
        sorted_fi = sorted(fi.items(), key=lambda x: x[1], reverse=True)
        fi_df = pd.DataFrame([
            {"Feature": PARAM_CONSTRAINTS[k]["desc"], "Importance (%)": v * 100}
            for k, v in sorted_fi
        ])
        st.bar_chart(fi_df.set_index("Feature"), color="#10b981")
        
    with col_chart2:
        st.markdown("#### 🎯 Evaluation Metrics Overview")
        if os.path.exists("models/confusion_matrix.png"):
            st.image("models/confusion_matrix.png", caption="Confusion Matrix on Test Dataset (2200 records)", use_container_width=True)
        else:
            st.info("Confusion matrix image generated during training.")

    st.markdown("#### 📚 Supported 22 Crop Categories")
    crop_chips = [
        f"{CROP_DETAILS.get(c, {}).get('icon', '🌱')} **{c.title()}** ({CROP_DETAILS.get(c, {}).get('category', 'Crop')})"
        for c in recommender.classes
    ]
    st.write(" • ".join(crop_chips))

# TAB 3: BATCH CSV PREDICTION
with tab_batch:
    st.markdown("### 📑 Batch Crop Recommendation Engine")
    st.write(
        "Upload a CSV file containing farm or regional soil test measurements to receive automated "
        "crop recommendations and confidence scores for multiple fields simultaneously."
    )
    
    st.markdown("##### Expected CSV Format:")
    sample_format = pd.DataFrame([{
        "N": 90, "P": 42, "K": 43, "temperature": 20.8, "humidity": 82.0, "ph": 6.5, "rainfall": 202.9
    }])
    st.dataframe(sample_format)
    
    uploaded_file = st.file_uploader("Upload soil & climate CSV file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            batch_df = pd.read_csv(uploaded_file)
            st.write(f"Loaded {len(batch_df)} rows. Processing predictions...")
            
            result_df = recommender.batch_recommend(batch_df)
            
            st.success("Batch classification completed successfully!")
            st.dataframe(result_df, use_container_width=True)
            
            csv_data = result_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Predictions CSV",
                data=csv_data,
                file_name="opticrop_batch_recommendations.csv",
                mime="text/csv"
            )
        except Exception as e:
            st.error(f"Error processing CSV: {e}")

# TAB 4: ABOUT & AGRONOMY GUIDE
with tab_about:
    st.markdown("### 🌾 About OptiCrop & Agronomic Fundamentals")
    st.markdown("""
    #### 1. Project Background
    Agriculture faces significant productivity challenges due to improper crop selection relative to soil chemistry 
    and microclimates. **OptiCrop** addresses this by employing a supervised **Random Forest Classifier** trained 
    on multi-parameter agricultural data.
    
    #### 2. Key Agricultural Drivers
    - **Nitrogen (N):** Vital for chlorophyll synthesis, vegetative leaf area, and protein content. Deficiencies lead to chlorosis and stunted growth.
    - **Phosphorus (P):** Fundamental for ATP energy transfer, rapid early root establishment, flowering, and seed maturation.
    - **Potassium (K):** Regulates stomatal opening, enzymatic activation, drought tolerance, and fruit size/disease resistance.
    - **Soil pH:** Dictates nutrient bioavailability. Extreme pH locks up micronutrients even if present in the soil.
    - **Temperature & Humidity:** Govern plant transpiration rate, pollen viability, and photosynthetic enzyme activity.
    - **Rainfall:** Determines water balance, vegetative vigor, and harvest viability.
    
    #### 3. Future Enhancements
    - **Soil Texture Integration:** Inclusion of sand, silt, and clay percentage fractions.
    - **Real-Time Weather API Integration:** Automatic GPS-based weather fetching.
    - **Market Economics:** Crop profitability and regional market price forecasts.
    - **Satellite Remote Sensing:** Multi-spectral NDVI vegetation health tracking.
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6b7280; font-size: 0.9rem;'>"
    "OptiCrop – Intelligent Crop Recommendation System • Developed with Python, Scikit-Learn & Streamlit"
    "</div>",
    unsafe_allow_html=True
)
