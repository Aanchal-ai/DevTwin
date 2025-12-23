import streamlit as st
import streamlit.components.v1 as components
import re

# --- UI CONFIG ---
st.set_page_config(page_title="DevTwin Pro | Final Stable", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    .hero-title {
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        font-size: 48px; font-weight: 800; text-align: center;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0ea5e9, #6366f1);
        color: white; border-radius: 25px; border: none; padding: 12px;
        font-weight: bold; width: 100%; transition: 0.3s;
    }
    .metric-card {
        background: #1e293b; padding: 15px; border-radius: 10px;
        border-left: 5px solid #38bdf8; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def render_flowchart(mermaid_code):
    html = f"""
    <div class="mermaid" style="background: white; padding: 20px; border-radius: 12px;">{mermaid_code}</div>
    <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
    <script>mermaid.initialize({{startOnLoad:true, theme:'neutral'}});</script>
    """
    components.html(html, height=450, scrolling=True)

# --- MAIN INTERFACE ---
st.markdown('<h1 class="hero-title">DevTwin AI Engine</h1>', unsafe_allow_html=True)

with st.sidebar:
    st.header("📂 Smart Injection")
    uploaded_files = st.file_uploader("Upload Files (.java, .py, .class, etc.)", accept_multiple_files=True)
    st.divider()
    mode = st.selectbox("Intelligence Mode", ["Architecture Map", "Security Audit", "Modernization Score"])
    run_btn = st.button("START ANALYSIS 🔥")

if uploaded_files:
    text_code_only = ""
    valid_text_files = []
    all_file_names = []
    binary_count = 0
    
    # --- SMART FILTERING LOGIC ---
    for f in uploaded_files:
        all_file_names.append(f.name)
        try:
            # Phele check karenge ki kya ye text file hai
            content = f.read().decode('utf-8')
            text_code_only += f"\n--- {f.name} ---\n" + content + "\n"
            valid_text_files.append(f.name)
        except:
            # Agar binary hai toh sirf count badhayenge, context kharab nahi karenge
            binary_count += 1
            f.seek(0) # File pointer reset

    st.subheader(f"📊 Live Processing Hub")
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Uploads", len(uploaded_files))
    m2.metric("Source Files", len(valid_text_files))
    m3.metric("Compiled (Skipped)", binary_count)

    if run_btn:
        if not valid_text_files:
            st.error("Bhai, analysis ke liye kam se kam ek source file (.java, .py) chahiye. Compiled files analyze nahi ho sakti.")
        else:
            with st.spinner(f"Running {mode}..."):
                if mode == "Architecture Map":
                    # Dynamic Flowchart Generation
                    nodes = "\n".join([f"F{i}[{name}]" for i, name in enumerate(valid_text_files)])
                    mermaid_logic = f"graph TD\n    Start[User Code] --> Engine[DevTwin]\n    Engine --> Analysis[Logic Processing]\n    Analysis --> {valid_text_files[0]}\n    {nodes}"
                    render_flowchart(mermaid_logic)
                    st.success("Logic architecture mapped from source files.")

                elif mode == "Security Audit":
                    # Scan only text_code_only
                    findings = []
                    if re.search(r'(password|api_key|secret)\s*=\s*["\']', text_code_only, re.I):
                        findings.append("🔴 **Critical:** Hardcoded credentials in source.")
                    if "eval(" in text_code_only or "exec(" in text_code_only:
                        findings.append("🔴 **High Risk:** Dynamic code execution detected.")
                    
                    if findings:
                        for f in findings: st.markdown(f'<div class="metric-card">{f}</div>', unsafe_allow_html=True)
                    else:
                        st.success("No vulnerabilities found in source files.")

                elif mode == "Modernization Score":
                    score = 90 if binary_count == 0 else 75
                    st.title(f"Score: {score}/100")
                    st.progress(score / 100)
                    st.info("Tip: Source code looks good. Binary files in repo reduce modernization score.")
else:
    st.info("Files upload kijiye demo start karne ke liye.")