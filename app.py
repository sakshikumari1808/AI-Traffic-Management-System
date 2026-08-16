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
    
import streamlit as st

st.set_page_config(
    page_title="AI Traffic Management System",
    page_icon="🚦",
    layout="wide"
)

# ==========================================
# HEADER
# ==========================================

st.title("🚦 AI Traffic Management System")

st.markdown("""
### Intelligent Traffic Monitoring using YOLO11 and OpenCV

This project uses Artificial Intelligence and Computer Vision to detect vehicles,
count traffic volume, and estimate traffic density from traffic videos.

Developed as part of the IBM Internship / Training Program.
""")

st.divider()

# ==========================================
# PROJECT DESCRIPTION
# ==========================================

st.header("📖 Project Description")

st.write("""
Traffic congestion is a major problem in urban areas.
This project uses the YOLO11 object detection model and OpenCV
to automatically detect vehicles from traffic footage.

The system:

- Detects vehicles in video frames
- Counts vehicles in real time
- Classifies traffic density
- Generates an annotated output video
- Helps support intelligent traffic management decisions
""")

# ==========================================
# FEATURES
# ==========================================

st.header("✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
✅ Vehicle Detection

✅ Vehicle Counting

✅ Traffic Density Analysis

✅ YOLO11 Object Detection

✅ OpenCV Video Processing
    """)

with col2:
    st.markdown("""
✅ Real-Time Frame Analysis

✅ Automated Video Processing

✅ Output Video Generation

✅ Smart Traffic Monitoring

✅ AI-Based Decision Support
    """)

st.divider()

# ==========================================
# TECHNOLOGY STACK
# ==========================================

st.header("🛠 Technology Stack")

st.markdown("""
- **Python**
- **YOLO11 (Ultralytics)**
- **OpenCV**
- **NumPy**
- **Streamlit**
- **Google Colab**
- **GitHub**
""")

st.divider()

# ==========================================
# SCREENSHOTS
# ==========================================

st.header("📸 Project Screenshots")

st.info(
    "Upload screenshots to the 'screenshots' folder in your GitHub repository "
    "and update the image filenames below."
)

try:
    st.image("screenshots/output1.png", caption="Vehicle Detection")
except:
    pass

try:
    st.image("screenshots/output2.png", caption="Traffic Density Analysis")
except:
    pass

st.divider()

# ==========================================
# LIVE DEMO
# ==========================================

st.header("🎥 Demo Section")

uploaded_file = st.file_uploader(
    "Upload a traffic video",
    type=["mp4"]
)

if uploaded_file is not None:
    st.success("Video uploaded successfully!")
    st.video(uploaded_file)

st.info(
    "In the full implementation, the uploaded video is processed "
    "using YOLO11 to detect vehicles and calculate traffic density."
)

st.divider()

# ==========================================
# PROJECT OUTCOME
# ==========================================

st.header("📊 Project Outcome")

st.write("""
The system successfully:

- Detects Cars, Motorcycles, Buses, and Trucks
- Counts vehicles automatically
- Classifies traffic density as:
  - LOW
  - MEDIUM
  - HIGH
- Produces an annotated output video
""")

st.divider()

# ==========================================
# GITHUB
# ==========================================

st.header("🔗 Project Links")

st.markdown("""
**GitHub Repository**

https://github.com/sakshikumari1808/AI-Traffic-Management-System
""")

st.success("IBM Internship Project Submission Ready ✅")
