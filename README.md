# 🌱 Crop Recommendation System

An AI-powered machine learning application that recommends the most suitable crop based on soil nutrients and environmental conditions.

## 📌 Project Overview

The Crop Recommendation System uses a Machine Learning model to analyze soil and environmental parameters and recommend an appropriate crop.

The application provides a simple and interactive web interface built using Streamlit.

## 🚀 Features

- 🌱 Crop recommendation using Machine Learning
- 📊 Uses soil nutrient information
- 🌡️ Considers temperature and humidity
- 💧 Considers rainfall
- 🧪 Considers soil pH
- 🤖 Random Forest classification model
- 🎨 Interactive Streamlit interface
- ⚡ Real-time prediction

## 🧠 Machine Learning

The project uses a **Random Forest Classifier**.

### Input Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- Soil pH
- Rainfall

### Output

The model recommends a suitable crop based on the provided conditions.

## 📂 Project Structure

```text
Crop-Prediction-System/
│
├── data/
│   └── Crop_recommendation.csv
│
├── app.py
├── train_model.py
├── crop_model.pkl
├── requirements.txt
├── README.md
└── .gitignore