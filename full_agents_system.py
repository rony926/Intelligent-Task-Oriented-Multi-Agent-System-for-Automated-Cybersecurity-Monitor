import os
import json
import uuid
from datetime import datetime
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import IsolationForest

# -------------------------------------------------------------------
# CollectorAgent (Ubuntu logs from /var/log/auth.log)
# -------------------------------------------------------------------
class CollectorAgent:
    def collect_logs(self):
        logs = []

        # Ubuntu auth.log path
        log_file = "/var/log/auth.log"

        if os.path.exists(log_file):
            try:
                with open(log_file, "r") as f:
                    for line in f.readlines()[-100:]:  # last 100 lines
                        logs.append(line.strip())
            except PermissionError:
                print("Permission denied: run the script with sudo to read auth.log")
        else:
            print(f"{log_file} not found. Using sample logs.")
            # Sample logs if auth.log not accessible
            logs = [
                "Failed SSH login from 164.92.75.21",
                "User root executed suspicious command: nc -lvnp 4444",
                "Large outbound traffic to 103.221.55.9",
                "Normal cron job executed",
                "User john logged in successfully"
            ]
        return logs

# -------------------------------------------------------------------
# DetectionAgent with ML
# -------------------------------------------------------------------
class DetectionAgent:
    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = IsolationForest(contamination=0.3, random_state=42)

    def train_model(self, logs):
        X = self.vectorizer.fit_transform(logs)
        self.model.fit(X)

    def detect(self, logs):
        self.train_model(logs)

        results = []
        X_test = self.vectorizer.transform(logs)
        preds = self.model.predict(X_test)

        for i, log in enumerate(logs):
            if preds[i] == -1:
                severity = "high" if "nc -lvnp" in log or "Large outbound" in log else "medium"
                risk = 90 if severity == "high" else 60
                results.append({
                    "id": str(uuid.uuid4()),
                    "type": "Anomalous Activity",
                    "log": log,
                    "severity": severity,
                    "risk": risk
                })
        return results

# -------------------------------------------------------------------
# ThreatIntelAgent
# -------------------------------------------------------------------
class ThreatIntelAgent:
    mitre_map = {
        "Anomalous Activity": "TA0001 - Initial Access"
    }

    def enrich(self, detections):
        for d in detections:
            d["mitre"] = self.mitre_map.get(d["type"], "Unknown")
        return detections

# -------------------------------------------------------------------
# AnalystAgent
# -------------------------------------------------------------------
class AnalystAgent:
    def analyze(self, enriched):
        analysis = {
            "total_incidents": len(enriched),
            "high_risk": sum(1 for e in enriched if e["risk"] >= 80),
            "summary": []
        }
        for e in enriched:
            analysis["summary"].append({
                "id": e["id"],
                "type": e["type"],
                "event": e["log"],
                "severity": e["severity"],
                "risk_score": e["risk"],
                "mitre": e["mitre"]
            })
        return analysis

# -------------------------------------------------------------------
# ReportAgent
# -------------------------------------------------------------------
class ReportAgent:
    def generate_text(self, analysis):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M")
        text_report = f"=== EXECUTIVE SECURITY REPORT ===\nGenerated: {ts}\n\n"
        text_report += f"Total Incidents: {analysis['total_incidents']}\n"
        text_report += f"High Risk Incidents: {analysis['high_risk']}\nDetails:\n"

        for item in analysis["summary"]:
            text_report += f"""
Incident ID: {item['id']}
Type: {item['type']}
Event: {item['event']}
Severity: {item['severity']}
Risk Score: {item['risk_score']}
MITRE Technique: {item['mitre']}
--------------------------------------------
"""
        text_report += "\nRecommendations:\n- Monitor anomalous events closely\n- Investigate suspicious network activity\n- Apply security patches\n"
        return text_report

    def generate_json(self, analysis):
        return json.dumps(analysis, indent=4)

# -------------------------------------------------------------------
# CoordinatorAgent
# -------------------------------------------------------------------
class CoordinatorAgent:
    def run(self):
        collector = CollectorAgent()
        detector = DetectionAgent()
        intel = ThreatIntelAgent()
        analyst = AnalystAgent()
        reporter = ReportAgent()

        logs = collector.collect_logs()
        detections = detector.detect(logs)
        enriched = intel.enrich(detections)
        analysis = analyst.analyze(enriched)

        text_report = reporter.generate_text(analysis)
        json_report = reporter.generate_json(analysis)

        return text_report, json_report

# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------
if __name__ == "__main__":
    system = CoordinatorAgent()
    text, json_data = system.run()
    print(text)

    with open("ml_ubuntu_security_report.json", "w") as f:
        f.write(json_data)

    print("\nJSON report saved as ml_ubuntu_security_report.json")
