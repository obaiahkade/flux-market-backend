"""
URL configuration for ecommerce_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# ecommerce_platform/urls.py
from django.contrib import admin
from django.urls import path
from core_marketplace.views import (
    log_dashboard, 
    insert_log, 
    insert_bulk_logs,
    get_anomalies,
    get_high_risk
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', log_dashboard, name='dashboard'),
    
    # API endpoints for logs
    path('api/insert-log/', insert_log, name='insert_log'),
    path('api/insert-bulk-logs/', insert_bulk_logs, name='insert_bulk_logs'),
    path('api/anomalies/', get_anomalies, name='get_anomalies'),
    path('api/high-risk/', get_high_risk, name='get_high_risk'),
]
