CREATE TABLE IF NOT EXISTS system_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    service_name VARCHAR(50),
    log_message TEXT,
    severity VARCHAR(10),
    ai_risk_score FLOAT,
    is_anomaly BOOLEAN
);