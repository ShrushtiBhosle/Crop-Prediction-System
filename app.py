import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Load trained model
# -----------------------------
with open("crop_model.pkl", "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="wide"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #9aa0a6;
        margin-bottom: 35px;
    }

    .result-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        background-color: #1f2937;
        margin-top: 25px;
    }

    .result-title {
        font-size: 20px;
        color: #9ca3af;
    }

    .crop-name {
        font-size: 36px;
        font-weight: bold;
    }

    .info-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #111827;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="main-title">🌱 Crop Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered crop recommendation based on soil and environmental conditions</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Input section
# -----------------------------
st.subheader("🌾 Enter Crop Conditions")

col1, col2 = st.columns(2)

with col1:
    nitrogen = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        max_value=150.0,
        value=50.0
    )

    phosphorus = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        max_value=150.0,
        value=50.0
    )

    potassium = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        max_value=150.0,
        value=50.0
    )

    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=50.0,
        value=25.0
    )

with col2:
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0
    )

    ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=300.0,
        value=100.0
    )

# -----------------------------
# Prediction
# -----------------------------
st.write("")

if st.button("🌱 Recommend Crop", use_container_width=True):

    input_data = pd.DataFrame(
        [[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    )

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-title">Recommended Crop</div>
            <div class="crop-name">🌾 {prediction.capitalize()}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success(
        f"The model recommends **{prediction.capitalize()}** based on the provided conditions."
    )

# -----------------------------
# Model information
# -----------------------------
st.markdown("---")

st.subheader("🤖 About the Model")

st.markdown("""
<div class="info-box">

<strong>Algorithm:</strong> Random Forest Classifier<br><br>

<strong>Input Features:</strong> Nitrogen, Phosphorus, Potassium,
Temperature, Humidity, Soil pH and Rainfall<br><br>

<strong>Purpose:</strong> Recommend a suitable crop based on soil
nutrients and environmental conditions.

</div>
""", unsafe_allow_html=True)