import streamlit as st

st.title("AI Traffic Management System")

st.write("""
This project uses YOLO11 and OpenCV for vehicle detection
and traffic density analysis.
""")

uploaded_file = st.file_uploader("Upload a traffic video", type=["mp4"])

if uploaded_file is not None:
    st.success("Video uploaded successfully!")
    st.video(uploaded_file)
