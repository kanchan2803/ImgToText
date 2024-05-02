import cv2
import numpy as np
import streamlit as st
import main


#ui
st.title("Text Recognition from Image")

#for camera input
st.header("Camera Input")

pic = st.camera_input("Capture image")

if pic is not None:
    bytes_data = pic.read()

    np_array = np.frombuffer(bytes_data,np.uint8)

    image = cv2.imdecode(np_array,cv2.IMREAD_COLOR)

    cv2.imwrite("cap_img.jpg",image)

    one,two =st.columns(2)
    with one:
        st.image(pic, caption='Uploaded Image')
        st.write("Image saved successfully.")
    
    processed_image, text = main.extract_text("cap_img.jpg")
    with two:
        st.image(processed_image, caption='Processed Image')
        st.write("Image Processed.")
    
    st.subheader("Extracted Text:")
    st.code(text)

st.divider()

#add to upload img from user
st.header("File Input")

uploaded_file = st.file_uploader("Upload image:",type=["jpg","png","jpeg"]) 

if uploaded_file is None:
    st.write("NO image is Uploaded!!")

if uploaded_file is not None:
    bytes_data = uploaded_file.read()

    # Convert bytes to a NumPy array
    np_array = np.frombuffer(bytes_data, np.uint8)

    # Decode the NumPy array as a OpenCV image (BGR color space)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    # Save the image to a specified location
    temp_image_path="captured_image.jpg"
    cv2.imwrite(temp_image_path,image)
    
    #creating columns
    one,two =st.columns(2)

    # Display the uploaded image
    with one:
        st.image(uploaded_file, caption='Uploaded Image')
        st.write("Image saved successfully.")
    
    processed_image, text = main.extract_text(temp_image_path)
    with two:
        st.image(processed_image, caption='Processed Image')
        st.write("Image Processed.")
    
    st.subheader("Extracted Text:")
    st.code(text)

st.divider()
st.write("Made with 🧠 and 🍯 by Naive Bees 🐝")
