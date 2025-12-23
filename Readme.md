# 🚀 DevTwin Pro AI - Legacy Code Intelligence Engine

**DevTwin Pro AI** ek powerful aur lightweight tool hai jo legacy codebase ko samajhne, modernize karne aur secure banane mein developers ki madad karta hai. Yeh tool complex source code ko instant visual maps (Flowcharts) mein badal deta hai aur deep security audits provide karta hai.

## 🔗 Live Demo
Check out the live application: [**Live Demo Link**](https://devtwin-mpmjeyx59g2qter8akkmxb.streamlit.app/)

---

## 🌟 Key Features

- **📊 Architecture Mapping:** Kisi bhi code repository ka real-time logical flowchart generate karta hai (Powered by Mermaid.js).
- **🛡️ Automated Security Audit:** Code mein chhupay gaye hardcoded secrets, passwords, aur dangerous functions (like `eval()`) ko instantly detect karta hai.
- **📈 Modernization Scoring:** Code ki quality, modularity aur documentation ke basis par ek "Modernization Score" deta hai jo refactoring mein help karta hai.
- **🛡️ Resilience & Robustness:** Yeh tool itna smart hai ki `.class` ya `.exe` jaisi binary files upload hone par bhi crash nahi hota, balki unhe intelligently skip kar deta hai.
- **☁️ Zero Setup:** Poori tarah browser-based hai, developers ko koi local environment setup karne ki zaroorat nahi.

---

## 🛠️ Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/) (Python-based Web Framework)
- **Visualization:** [Mermaid.js](https://mermaid.js.org/) (Real-time diagram generation)
- **Logic Engine:** Python (Regex-based pattern matching & logic processing)
- **Deployment:** Streamlit Community Cloud & GitHub

---

## 🚀 How to Use

1. **Upload Files:** Sidebar mein jao aur apni source code files (.java, .py, .js, etc.) upload karo.
2. **Select Mode:** Choose karo ki aapko Architecture Map dekhna hai, Security Audit karni hai, ya Modernization Score check karna hai.
3. **Analyze:** "START ANALYSIS" button par click karo aur results ko real-time mein dekho.

---

## 📂 Project Structure

```text
├── devtwin_app.py      # Main Application logic
├── requirements.txt    # Required Python libraries
└── README.md           # Project Documentation
