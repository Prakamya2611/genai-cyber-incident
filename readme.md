GenAI Cyber Incident Reporting System

A FastAPI-based, industry-ready cybersecurity incident analysis and reporting system that converts raw security logs into structured incident reports with severity scoring and PDF export, designed for SOC (Security Operations Center) workflows.

⚠️ This system generates draft reports only and follows a human-in-the-loop model for safety and compliance.

🚀 Problem Statement (SIH / Industry Context)

Security Operations Centers (SOCs) receive large volumes of heterogeneous logs (firewall, authentication, phishing alerts).
Manually correlating these logs and writing incident reports is:

Time-consuming

Error-prone

Inconsistent across analysts

This delays incident response and impacts investigation quality.

💡 Solution Overview

This project provides an automated cyber incident reporting backend that:

Correlates multiple security logs

Classifies incident type

Calculates severity using rule-based logic

Generates structured, professional incident reports

Exports reports as PDF for audits and compliance

The system is offline-capable, secure, and deployable in restricted environments.

✨ Key Features

🔍 Log Correlation Engine
Correlates firewall logs, authentication failures, and phishing alerts.

⚠️ Severity Scoring Logic
Rule-based classification (Low / Medium / High).

🧠 GenAI-Style Report Generation (Offline)
Produces human-readable incident summaries without external APIs.

🌐 FastAPI Backend
REST API with Swagger UI for easy testing and integration.

📄 PDF Export
One-click export of incident reports for SOC workflows.

🔐 Human-in-the-Loop Design
No automated enforcement actions — analyst review required.

🏗️ System Architecture
Security Logs (JSON)
        ↓
Log Correlation Engine
        ↓
Incident Classification & Severity Scoring
        ↓
Incident Report Generator
        ↓
API Response / PDF Export

🧰 Tech Stack

Backend: Python, FastAPI

API Testing: Swagger UI

PDF Generation: ReportLab

Deployment: Uvicorn

Architecture Style: Lightweight, flat structure

📂 Project Structure
genai-cyber-incident/
│
├── app.py              # Complete FastAPI application
├── requirements.txt    # Dependencies
└── README.md           # Documentation

▶️ How to Run Locally
1️⃣ Install dependencies
pip install fastapi uvicorn reportlab

2️⃣ Start the server
uvicorn app:app --reload

3️⃣ Open Swagger UI

👉 http://127.0.0.1:8000/docs

🔌 API Endpoints
🔹 POST /analyze

Analyzes logs and returns a structured incident report.

Input:
Firewall logs, authentication logs, phishing alerts (JSON)

Output:

Incident type

Severity

Indicators of Compromise (IOCs)

Timeline

Full incident report

🔹 POST /export/pdf

Generates and downloads a PDF incident report.

Output:

incident_report.pdf

🧪 Example Use Cases

SOC incident documentation

Cyber forensic reporting

Compliance and audit evidence

Internal security monitoring tools

🔐 Security & Compliance Notes

No external AI calls (offline-safe)

No automatic remediation

Analyst review required before action

Suitable for restricted / air-gapped environments

📌 Future Enhancements

Role-based access control (RBAC)

SIEM integrations (Splunk / ELK)

Local LLM integration

Incident database & dashboard

🏆 Why This Project Stands Out

✔ Industry-usable backend
✔ SIH-ready problem statement
✔ Realistic SOC design
✔ Clean, professional API
✔ Not a toy or demo project

👤 Author

Prakamya
Built as an industry-grade cybersecurity backend project with real-world applicability.