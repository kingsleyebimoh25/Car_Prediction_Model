import streamlit as st 
from PIL import Image
# App title
st.title("BMI Calculator")
# Display image
image = Image.open("bmi_image_png_")
st.image(image, caption="Body Mass Index Illustration",
use_container_width=True)
# Input fields
name = st.text_import("Enter your name")
height = st.number_input("Enter your height (in cm):", format="%.2f")
weight = st.number_input("Enter your weight (in kg):", format=%.2f)
# Calculate BMI
if st.button("Calculate BMI"):
    if height > 0:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
        elif 25 <= bmi < 29.9:
        category = "Overweight"
        else:
        category = "Obese"
        st.success(f"{name}, your BMI is {bmi:.2f} which is considered{category}")
    else:
        st.error("please enter a valid height")