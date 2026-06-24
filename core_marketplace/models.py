from django.db import models

class SystemLog(models.Model):
    service_name = models.CharField(max_length=100) 
    log_message = models.TextField()
    severity = models.CharField(max_length=20)     
    ai_risk_score = models.FloatField(default=0.0)
    is_anomaly = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.severity}] {self.service_name} - {self.log_message[:30]}"