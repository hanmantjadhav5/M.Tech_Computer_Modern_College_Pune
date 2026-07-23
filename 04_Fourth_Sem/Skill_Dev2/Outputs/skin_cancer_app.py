import streamlit as st
from PIL import Image
import numpy as np
import random

st.title("Skin Cancer Detection Dashboard")

st.write("Upload a skin lesion image to analyze.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

classes = [
    "Melanoma",
    "Melanocytic Nevi",
    "Basal Cell Carcinoma",
    "Actinic Keratosis",
    "Benign Keratosis"
]

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Demo prediction (random for assignment)
    prediction = random.choice(classes)
    confidence = random.randint(80,99)

    st.subheader("Prediction Result")

    st.write("Predicted Class:", prediction)
    st.write("Confidence:", confidence,"%")

    if prediction == "Melanoma":
        st.error("High Risk Skin Cancer")
    else:
        st.success("Low Risk Lesion")