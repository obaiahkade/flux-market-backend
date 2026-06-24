import requests
import time
import random

# మీ Django API URL
URL = "http://127.0.0.1:8000/api/insert-log/"

services = ["Auth-Service", "Payment-Gateway", "Database-Cluster", "AI-Anomaly-Detector", "Firewall-v10"]
messages = [
    "User login successful from approved IP.",
    "Database connection pool peaked at 85%.",
    "High latency detected on checkout API endpoint.",
    "Multiple failed SSH login attempts detected from unknown country.",
    "SQL Injection signature detected and dropped by firewall."
]
severities = ["INFO", "WARNING", "ERROR", "CRITICAL"]

print("🚀 Starting Live Mock Log Streamer... (Press Ctrl+C to stop)")

while True:
    severity = random.choice(severities)
    is_anomaly = True if severity in ["ERROR", "CRITICAL"] else False
    ai_risk = round(random.uniform(0.7, 0.99), 2) if is_anomaly else round(random.uniform(0.05, 0.4), 2)
    
    payload = {
        "service_name": random.choice(services),
        "log_message": random.choice(messages),
        "severity": severity,
        "ai_risk_score": ai_risk,
        "is_anomaly": is_anomaly
    }
    
    try:
        response = requests.post(URL, json=payload)
        if response.status_code == 200:
            print(f"✅ Sent: [{severity}] - {payload['service_name']} -> Live Dashboard Updated!")
        else:
            print(f"❌ Failed to send log: {response.text}")
    except Exception as e:
        print(f"⚠️ Error connecting to server: {e}")
        
    time.sleep(3)