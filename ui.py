import streamlit as st
from pathlib import Path
import base64

# Custom CSS for styling
st.markdown("""
    <style>
    .big-title {
        font-size: 60px !important;
        color: #2E86C1 !important;
        text-align: center;
        padding: 30px;
    }
    .highlight {
        background-color: #F9E79F;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .section-header {
        font-size: 36px !important;
        color: #27AE60 !important;
        border-bottom: 3px solid #2E86C1;
        padding-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Main title
st.markdown('<p class="big-title">🚀 WebAutomation Pro Suite 2.0</p>', unsafe_allow_html=True)
st.markdown("### The Future of Reliable Web Testing & Automation", unsafe_allow_html=True)

# Hero Section
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ## ⚡ **One-Click Web Testing Revolution** ⚡
        **Transform your web testing workflow** with our enterprise-grade automation suite featuring:
        - Instant environment setup
        - Cross-browser testing matrix
        - Self-healing test scripts
        - AI-powered element detection
        """)
        
        st.markdown("""
        <div class="highlight">
        💡 **Innovation Unleashed**: Experience 78% faster test execution with our parallel processing engine
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("https://cdn.pixabay.com/photo/2017/08/05/00/12/robot-2581613_1280.png", 
                width=300, caption="Your Automated Testing Assistant")

# Features Section
st.markdown('<p class="section-header">🌟 Why Choose WebAutomation Pro?</p>', unsafe_allow_html=True)

features = st.columns(3)
with features[0]:
    st.markdown("""
    ### 🧩 Zero-Config Setup
    **Unzip & Run** in 90 seconds:
    1. Download package
    2. Extract files
    3. `launch-suite.exe`
    """)

with features[1]:
    st.markdown("""
    ### 🔒 Military-Grade Reliability
    **99.99% Test Accuracy** through:
    - Multi-layer validation
    - Smart wait mechanisms
    - Automatic retry systems
    """)

with features[2]:
    st.markdown("""
    ### 🌐 Universal Compatibility
    Works seamlessly with:
    - All modern browsers
    - CI/CD pipelines
    - Cloud test grids
    - Legacy systems
    """)

# Demo Section
st.markdown('<p class="section-header">🎥 See It In Action</p>', unsafe_allow_html=True)
st.video("https://example.com/demo-video.mp4")  # Replace with actual demo video URL

# Download Section
st.markdown('<p class="section-header">📥 Get Started Now</p>', unsafe_allow_html=True)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/zip;base64,{bin_str}" download="{bin_file}">Download {file_label}</a>'
    return href

st.markdown("""
    ### 🚨 Limited Time Offer
    Download our complete suite including:
    - Automation framework
    - Sample test cases
    - Setup wizard
    - Documentation
    """)

st.markdown(get_binary_file_downloader_html('WebAutomationPro.zip', 'WebAutomation Pro Suite'), 
           unsafe_allow_html=True)

# Testimonial Section
st.markdown('<p class="section-header">💬 What Users Say</p>', unsafe_allow_html=True)
st.markdown("""
> "**Game Changer!** Reduced our regression testing time from 8 hours to 45 minutes!"
> 
> _- TechLead @ Fortune 500 Company_

> "The easiest automation setup we've ever used. Literally unzip and go!"
> 
> _- QA Manager @ Startup Inc._
""")

# Footer
st.markdown("---")
st.markdown("**Need Help?** Contact our 24/7 support team: support@webautomationpro.com")