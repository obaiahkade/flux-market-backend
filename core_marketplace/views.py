from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SystemLog
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def log_dashboard(request):
    
    return render(request, 'dashboard.html')
def create_and_broadcast_log(service_name, log_message, severity, ai_risk_score, is_anomaly):
  
    log = SystemLog.objects.create(
        service_name=service_name,
        log_message=log_message,
        severity=severity,
        ai_risk_score=ai_risk_score,
        is_anomaly=is_anomaly
    )
    

    channel_layer = get_channel_layer()
    if channel_layer:
        async_to_sync(channel_layer.group_send)(
            "logs",
            {
                "type": "log_message",
                "data": {
                    "id": log.id,
                    "service_name": log.service_name,
                    "log_message": log.log_message,
                    "severity": log.severity,
                    "ai_risk_score": log.ai_risk_score,
                    "is_anomaly": log.is_anomaly,
                    "timestamp": log.timestamp.strftime('%Y-%m-%d %H:%M:%S')
                }
            }
        )
    return log

@csrf_exempt
@require_http_methods(["POST"])
def insert_log(request):
    try:
        data = json.loads(request.body)
        log = create_and_broadcast_log(
            service_name=data.get('service_name', 'Unknown'),
            log_message=data.get('log_message', ''),
            severity=data.get('severity', 'INFO'),
            ai_risk_score=float(data.get('ai_risk_score', 0.0)),
            is_anomaly=bool(data.get('is_anomaly', False))
        )
        return JsonResponse({'status': 'success', 'message': 'Log created successfully', 'log_id': log.id})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def insert_bulk_logs(request):
    try:
        data = json.loads(request.body)
        logs_data = data.get('logs', [])
        created_logs = []
        for log_data in logs_data:
            log = create_and_broadcast_log(
                service_name=log_data.get('service_name', 'Unknown'),
                log_message=log_data.get('log_message', ''),
                severity=log_data.get('severity', 'INFO'),
                ai_risk_score=float(log_data.get('ai_risk_score', 0.0)),
                is_anomaly=bool(log_data.get('is_anomaly', False))
            )
            created_logs.append(log.id)
        return JsonResponse({'status': 'success', 'message': f'Created {len(created_logs)} logs', 'log_ids': created_logs})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@require_http_methods(["GET"])
def get_anomalies(request):
    try:
        limit = int(request.GET.get('limit', 50))
        anomalies = SystemLog.objects.filter(is_anomaly=True).order_by('-timestamp')[:limit]
        return JsonResponse({
            'status': 'success',
            'count': anomalies.count(),
            'data': [
                {
                    'id': log.id,
                    'service_name': log.service_name,
                    'log_message': log.log_message,
                    'severity': log.severity,
                    'ai_risk_score': log.ai_risk_score,
                    'timestamp': log.timestamp.isoformat()
                } for log in anomalies
            ]
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@require_http_methods(["GET"])
def get_high_risk(request):
    try:
        threshold = float(request.GET.get('threshold', 0.7))
        limit = int(request.GET.get('limit', 50))
        logs = SystemLog.objects.filter(ai_risk_score__gte=threshold).order_by('-timestamp')[:limit]
        return JsonResponse({
            'status': 'success',
            'threshold': threshold,
            'count': logs.count(),
            'data': [
                {
                    'id': log.id,
                    'service_name': log.service_name,
                    'log_message': log.log_message,
                    'severity': log.severity,
                    'ai_risk_score': log.ai_risk_score,
                    'timestamp': log.timestamp.isoformat()
                } for log in logs
            ]
        })
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)