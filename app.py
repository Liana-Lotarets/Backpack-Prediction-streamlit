import streamlit as st
import joblib
from feature_processing import *

# Завантаження моделі
model = joblib.load("backpack_prediction.pkl")

# Sidebar
st.sidebar.title(":primary[Backpack Price Prediction]")
st.sidebar.image("header.png",)
st.sidebar.markdown("Based on the materials of the")
st.sidebar.markdown(
    "***Backpack Prediction Challenge***, *Playground Series - Season 5, Episode 2.*"
)
st.sidebar.markdown(
    "The competition details on [kaggle](https://www.kaggle.com/competitions/playground-series-s5e2)."
)

# Main
st.title(":primary[Backpack Price Regression Model]")
col1, col2, col3, col4 = st.columns(4)
with col1:
    brand = st.selectbox(":orange[Brand]", brand_list)
with col2:
    style = st.selectbox(":orange[Style]", style_list)
with col3:
    material = st.selectbox(":orange[Material]", material_list)
with col4:
    color = st.selectbox(":rainbow[Color]", color_list)

col1, col2, col3 = st.columns(3)
with col1:
    size = st.selectbox(":orange[Size]", list(size_map.keys()))
with col2:
    laptop_compartment = st.selectbox(
        ":orange[Laptop Compartment]", list(laptop_compartment_map.keys())
    )
with col3:
    waterproof = st.selectbox(
        ":orange[Waterproof] :thunder_cloud_and_rain:", list(waterproof_map.keys())
    )

# st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    compartments = st.number_input(
        ":orange[Number of Compartments]", min_value=1, max_value=10, value=5, step=1
    )
with col2:
    weight_capacity = st.number_input(
        ":orange[Weight Capacity (kg)]",
        min_value=5.0,
        max_value=30.0,
        value=18.0,
        step=0.25,
    )

# Кнопка передбачення
if st.button(":green[Predict]"):
    features = make_feature_vector(
        brand,
        material,
        size,
        compartments,
        laptop_compartment,
        waterproof,
        style,
        color,
        weight_capacity,
    )
    prediction = model.predict([features])[0]
    st.success(f"Predicted price: {prediction.round(2)}")
