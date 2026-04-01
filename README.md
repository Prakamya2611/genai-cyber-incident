# 🚨 GenAI Cyber Incident Reporting System

An industry-ready FastAPI-based cybersecurity incident analysis and reporting system that converts raw security logs into structured incident reports with severity scoring and PDF export.

⚠️ This system generates draft reports only and follows a human-in-the-loop model for safety and compliance.

---

## 🚀 Live Demo

👉 https://genai-cyber-incident.onrender.com/static/index.html

---

## 💡 Problem Statement

Security Operations Centers (SOCs) deal with large volumes of logs (firewall, authentication, phishing alerts).

Manual analysis is:

* ⏱️ Time-consuming
* ❌ Error-prone
* 🔄 Inconsistent

This delays incident response and reduces investigation efficiency.

---

## 🧠 Solution

This system automates:

* 🔍 Log correlation
* ⚠️ Incident classification
* 📊 Severity scoring
* 📝 Report generation
* 📄 PDF export

All in a **secure, offline-capable environment**

---

## ✨ Features

* 🔍 Log Correlation Engine
* ⚠️ Rule-Based Severity Scoring
* 🧠 AI-style Incident Report Generation (offline)
* 🌐 FastAPI REST Backend
* 📄 PDF Export (ReportLab)
* 📂 File Upload + JSON Input
* 🎨 SOC-style Dashboard UI

---

## 🏗️ Architecture

```
Security Logs (JSON)
        ↓
Log Correlation Engine
        ↓
Incident Classification
        ↓
Report Generator
        ↓
API Response / PDF Export
```

---

## 🧰 Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** HTML, CSS, JavaScript
* **PDF Generation:** ReportLab
* **Deployment:** Render
* **API Testing:** Swagger UI

---

## 📂 Project Structure

```
genai-cyber-incident/
│
├── app.py
├── requirements.txt
├── static/
│   └── index.html
└── README.md
```

---

## ▶️ How to Run Locally

### 1️⃣ Install dependencies

```
pip install fastapi uvicorn reportlab
```

### 2️⃣ Run server

```
uvicorn app:app --reload
```

### 3️⃣ Open UI

```
http://127.0.0.1:8000/static/index.html
```

---

## 🔌 API Endpoints

### 🔹 POST `/analyze`

Analyzes logs and returns incident report.

### 🔹 POST `/export/pdf`

Generates downloadable PDF report.

---

## 🧪 Example Input

```json
{
  "firewall_logs": [{"src_ip": "192.168.1.1"}],
  "auth_logs": [{"user": "admin", "status": "FAILED"}],
  "phishing_alerts": [{"email": "user@test.com"}]
}
```

---

## 🔐 Security Notes

* No external AI APIs used
* Fully offline-capable
* No automatic remediation
* Analyst review required

---

## 📌 Future Enhancements

* 🔐 Role-Based Access Control (RBAC)
* 📊 Dashboard analytics (charts)
* 🔗 SIEM integrations (Splunk, ELK)
* 🧠 Local LLM integration

---

## 🏆 Highlights

✔ Real-world SOC use case
✔ Industry-style backend architecture
✔ Clean API design
✔ Full-stack working system
✔ Deployed and accessible online

---

## 👤 Author

**Prakamya**
Built as a real-world cybersecurity + GenAI project 🚀
