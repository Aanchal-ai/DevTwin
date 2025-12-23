import streamlit as st
import streamlit.components.v1 as components
import re

# --- UI CONFIG ---
st.set_page_config(page_title="DevTwin Pro | Full Intelligence", layout="wide")

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

# --- ANALYSIS ENGINES ---

def run_security_audit(code):
    findings = []
    # 1. Hardcoded Secrets
    if re.search(r'(password|api_key|secret|token)\s*=\s*["\'][^"\']+["\']', code, re.I):
        findings.append("🔴 **Critical:** Potential hardcoded credentials/secrets found.")
    # 2. SQL Injection Risk
    if "f\"select" in code.lower() or "+\"select" in code.lower():
        findings.append("🟠 **High:** Possible SQL Injection risk in raw queries.")
    # 3. Dangerous Functions
    if "eval(" in code or "exec(" in code:
        findings.append("🔴 **Critical:** Use of `eval()` or `exec()` detected (Remote Code Execution risk).")
    # 4. Debug Mode
    if "debug=True" in code:
        findings.append("🟡 **Medium:** Debug mode is enabled; disable for production.")
        
    return findings if findings else ["✅ No major security flaws detected by local scan."]

def calculate_modernization_score(code):
    score = 100
    suggestions = []
    
    lines = code.split('\n')
    # 1. Complexity
    if len(lines) > 300:
        score -= 20
        suggestions.append("- Code is too long (Monolithic). Break into modules.")
    # 2. Modern Standards
    if "async " not in code and "def " in code:
        score -= 10
        suggestions.append("- Use 'async/await' for better performance in modern Python.")
    # 3. Documentation
    if '"""' not in code and "'''" not in code:
        score -= 15
        suggestions.append("- Missing docstrings. Modern code requires clear documentation.")
        
    return max(score, 10), suggestions

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
    st.header("📂 Codebase Injection")
    uploaded_files = st.file_uploader("Upload Code Files", accept_multiple_files=True)
    st.divider()
    mode = st.selectbox("Intelligence Mode", ["Architecture Map", "Security Audit", "Modernization Score"])
    run_btn = st.button("START ANALYSIS 🔥")

if uploaded_files:
    full_code = ""
    file_list = [f.name for f in uploaded_files]
    for f in uploaded_files:
        full_code += f.read().decode('utf-8') + "\n"

    st.subheader(f"🧠 Analysis Output: {mode}")
    
    if run_btn:
        with st.spinner(f"Running {mode}..."):
            if mode == "Architecture Map":
                nodes = "\n".join([f"F{i}[{name}]" for i, name in enumerate(file_list)])
                mermaid_logic = f"graph TD\n    UI[User Interface] --> Engine[DevTwin Engine]\n    Engine --> Logic[Business Logic]\n    Logic --> {file_list[0]}\n    {nodes}"
                render_flowchart(mermaid_logic)
                st.success("System Architecture mapped successfully.")

            elif mode == "Security Audit":
                results = run_security_audit(full_code)
                for r in results:
                    st.markdown(f'<div class="metric-card">{r}</div>', unsafe_allow_html=True)
                st.warning("Note: This is a static scan. Manual review is recommended.")

            elif mode == "Modernization Score":
                score, tips = calculate_modernization_score(full_code)
                st.title(f"Score: {score}/100")
                st.progress(score / 100)
                st.subheader("How to improve:")
                for tip in tips:
                    st.write(tip)
                if score > 80: st.balloons()
else:
    st.info("Files upload karke 'START ANALYSIS' dabaiye.")