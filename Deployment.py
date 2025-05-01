import streamlit as st
import torch
import os
from PIL import Image
from ultralytics import YOLO

# Load the trained YOLO model
@st.cache_resource
def load_model():
    model_path = "best_Embryo_model.pt"  # Ensure correct path
    if not os.path.exists(model_path):
        st.error(f"Model file not found: {model_path}. Please check the path and try again.")
        return None  
    return YOLO(model_path)

# Initialize model
model = load_model()
if model is None:
    st.stop()  # Stop execution if model is missing

# Streamlit UI
st.title("🧬 Embryo Quality Prediction ")
st.write("Upload embryo images to predict their quality.")

# File uploader for multiple images
uploaded_files = st.file_uploader("Choose images...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        
        # Display uploaded image
        st.image(image, caption=f"Uploaded Image: {uploaded_file.name}", use_container_width=True)
        st.write("🔍 Processing...")

        # Perform inference
        results = model(image)  # Updated inference method

        # Extract classification results
        if hasattr(results[0], 'probs'):  
            predicted_class = results[0].probs.top1
            confidence_score = results[0].probs.top1conf
            class_names = model.names if hasattr(model, "names") else results[0].names
            st.success(f"✅ Predicted Quality: **{class_names[predicted_class]}** (Confidence: {confidence_score:.2f})")
        else:
            st.error("⚠️ Model output does not contain classification probabilities.")

# Run the app using:
# streamlit run App.py
