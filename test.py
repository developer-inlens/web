import streamlit as st

# Configure page
st.set_page_config(
    page_title="ReliAuto - Automation Foundation",
    layout="centered"
)

# Header Section
st.markdown("<h1 style='text-align: center'>ReliAuto Core</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'>Initial Release of Universal Automation Architecture</h3>", unsafe_allow_html=True)
st.markdown("---")

# Main Content
st.markdown("""
## **First-Step Automation Platform**

**Foundation Release Features:**
- Natural language instruction processing
- Cross-browser automation core
- Self-validating execution system
- macOS-optimized engine (Windows/Linux in development)
""")

st.markdown("---")

# Key Features
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### Design Philosophy
    *"Zero-code automation that scales"*
    - Plain English interface
    - Instant validation feedback
    - Fail-safe execution model
    - Enterprise-ready foundation
    """)

with col2:
    st.markdown("""
    ### Technical Foundation
    - Browser-native automation
    - Smart element detection
    - Execution analytics
    - Team workflow integration
    """)

# Download Section
st.markdown("---")
st.markdown("## Get Started with ReliAuto")
st.markdown("""
**Current Release Package (macOS):**
- Core automation engine
- Setup configuration wizard
- Sample test scenarios
- Debugging toolkit
- Documentation suite
""")

DOWNLOAD_URL = "https://1drv.ms/u/c/f4598138ab76194c/EZOtyBZorDNFjnwjCODpUVQBsgJSW-y-FxIM9-eQtAqpQg?e=N0H0u0"

st.markdown(f"""
<div style="text-align: center">
<a href="{DOWNLOAD_URL}">
    <button style="
        background: #1A5BC4;
        color: white;
        padding: 18px 32px;
        border: none;
        border-radius: 8px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        margin: 20px auto;
        display: block;">
        Download macOS Foundation (v1.0)
    </button>
</a>
</div>

**System Requirements:**  
- macOS 12+ (Intel/Apple Silicon)  
- Python 3.8+ • 4GB RAM minimum  
- Developer tools installed (Xcode Command Line Tools)
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
<a href="#"><i>Windows/Linux versions Q3 2024</i></a> • 
Support • Documentation • Security
</div>
""", unsafe_allow_html=True)