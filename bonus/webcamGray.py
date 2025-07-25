import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
with st.expander("Upload image"):
    # Upload image
    uploaded_image = st.file_uploader("Upload Image")

if  uploaded_image:
    # Create a pillow image instance
    img = Image.open(uploaded_image)
    # Convert the pillow image to grayscale
    gray_img = img.convert("L")
    # Render the graysclae image on the web page
    st.image(gray_img)

with st.expander("Start camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the graysclae image on the web page
    st.image(gray_img)
