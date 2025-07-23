# ThreatLens-Dashboard
atLens AI – Cyber Threat Dashboard

**ThreatLens AI** is a real-time cyber threat intelligence dashboard that uses OSINT and **Gemini AI** to fetch, summarize, and classify the severity of cyber threats from live social media posts.

Built as a **hackathon-ready MVP** using Streamlit.

---

## 🔍 Features

- 🔎 Search live social media for cybersecurity threats (e.g., "ransomware", "phishing")
- 🤖 Summarize threat posts using **Gemini AI**
- 🟢 Classify severity as Low / Medium / High
- 📊 Visualize results in a simple dashboard
- 🧠 Built with real-time OSINT (snscrape) and AI

---

## 💡 MVP Focus

> One data source. One dashboard. Live + AI + Insight.

This MVP is designed for:
- Hackathons
- AI proof-of-concepts
- Cybersecurity awareness
- Streamlit deployment

---

## 📦 Tech Stack

| Tool             | Purpose                        |
|------------------|--------------------------------|
| Python           | Core programming               |
| Streamlit        | UI / Dashboard framework       |
| snscrape         | Social media scraping          |
| Gemini API       | Threat summarization + scoring |
| pandas           | Data management                |
| dotenv           | API key management             |

---

## 🚀 How to Run Locally

### 1. Clone this repo

```bash
git clone https://github.com/DaisyGoyal/ThreatLens-Dashboard.git
cd ThreatLens-Dashboard
2. Install dependencies
pip install -r requirements.txt

3.Gemini API Key
GEMINI_API_KEY=AIzaSyCPmYfYxmosSbBTym3ENKj8ohZyapy9AhQ

4. Run the app

streamlit run app.py                                                                                                                                                                                                    
http://localhost:8501/
