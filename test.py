import streamlit as st

# Configure page
st.set_page_config(
    page_title="Project - Test Automation Suite",
    layout="centered"
)

# Header Section
st.markdown("<h1 style='text-align: center'>Project - Test Automation Suite</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center'>Help us build the easiest and most reliable automation suite</h3>", unsafe_allow_html=True)

# Workflow Section
st.markdown("""
## **How It Works**

1. **Install & Launch**  
   📥 Download → Launch Runner

2. **Configure Automation**  
   🖥️ Launch UI → Create browser workflows using visual designer

3. **Save Configuration**  
   💾 Name your workflow → Validate → Save (.tui format)

4. **Schedule Execution**  
   ⏲️ From Terminal: `schedule /path/to/<your config file>.tui`
""")

st.markdown("---")

# Key Features
# col1, col2 = st.columns(2)
# with col1:
#     st.markdown("""
#     ### Unmatched Simplicity
#     *"Automation should work for you, not vice versa"*
#     - 5-minute setup wizard
#     - Visual configuration dashboard
#     - Auto-dependency installation
#     - Guided troubleshooting
#     """)

# with col2:
#     st.markdown("""
#     ### Military-Grade Reliability
#     - Fail-safe execution protocol
#     - Automatic state recovery
#     - Precision validation layers
#     - Continuous integrity checks
#     """)

# Download Section
MACOS_URL = "https://1drv.ms/u/c/f4598138ab76194c/EZOtyBZorDNFjnwjCODpUVQBsgJSW-y-FxIM9-eQtAqpQg?e=N0H0u0"
WINDOWS_URL = "https://1drv.ms/u/c/f4598138ab76194c/EaN3mFLYcoZNleThW7aUuSUBc6eQMgM4SmFNva1-OY-7mw?e=Jqaccj"

dl1, dl2 = st.columns(2)
with dl1:
    st.markdown(f"""
    <div style="text-align: center">
    <a href="{MACOS_URL}">
        <button style="
            background: #1A5BC4;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin: 10px auto;
            display: block;
            width: 100%;">
            Download for macOS
        </button>
    </a>
    </div>
    """, unsafe_allow_html=True)

with dl2:
    st.markdown(f"""
    <div style="text-align: center">
    <a href="{WINDOWS_URL}">
        <button style="
            background: #107C10;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            margin: 10px auto;
            display: block;
            width: 100%;">
            Download for Windows
        </button>
    </a>
    </div>
    """, unsafe_allow_html=True)