# Intelligent-Task-Oriented-Multi-Agent-System-for-Automated-Cybersecurity-Monitor
This capstone project focuses on designing and implementing an Intelligent Multi-Agent System (MAS) that can autonomously monitor system sec
🛡️ Multi-Agent Cybersecurity Monitoring System
Agents Intensive – Capstone Project

This project implements an autonomous, multi-agent cybersecurity monitoring system designed to collect logs, detect anomalies, identify threats, map activity to the MITRE ATT&CK framework, and generate executive security reports.
It demonstrates how enterprise-grade AI agents can automate SOC (Security Operations Center) workflows.

🚀 Features

Collector Agent – Extracts system/network logs.

Detection Agent – Identifies suspicious activity (e.g., brute-force, reverse-shell).

Threat Intel Agent – Maps threats to MITRE ATT&CK categories.

Analyst Agent – Generates threat summaries and severity analysis.

Report Agent – Produces executive-level security reports.

Coordinator Agent – Orchestrates the entire workflow end-to-end.

🧩 Architecture Diagram

The project includes a full architecture diagram:

Collector → Detection → Threat Intel → Analyst → Report → Coordinator


A PNG version is included in the repository for visualization.

📂 Project Structure
│── full_agents_system.py
│── requirements.txt
│── README.md

🧠 How It Works

CollectorAgent reads system logs.

DetectionAgent scans log entries for anomalies.

ThreatIntelAgent enriches detections with MITRE ATT&CK references.

AnalystAgent evaluates severity and prepares summaries.

ReportAgent generates a final executive report.

CoordinatorAgent runs everything automatically.

🛠️ Installation

Clone the repository:

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

Linux / macOS:

python3 -m venv venv
source venv/bin/activate


Windows (CMD):

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt


Run the system:

python3 full_agents_system.py

📜 Example Output
Executive Security Report
Generated: 2025-01-01 11:00

- Brute Force detected: Failed SSH login ...
- Reverse Shell Attempt detected: suspicious netcat command ...

Recommendations:
- Enable fail2ban
- Block suspicious IPs
- Enforce MFA for root access

🧭 Submission Track (Agents Intensive)

Enterprise Agents Track
This project fits the Enterprise Track because it automates cybersecurity workflows, integrates multiple AI-driven agents, and simulates real SOC operations.

🧪 Future Enhancements

Real-time SIEM integration

Dashboard UI for SOC teams

Automated remediation agent

LLM-powered anomaly detection
