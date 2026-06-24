#!/usr/bin/env python
"""
Startup script for Daphne server with Django Channels
"""
import os
import sys
import django
from daphne.cli import CommandLineInterface

if __name__ == "__main__":
    # Set Django settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_platform.settings')
    
    # Setup Django
    django.setup()
    
    # Run Daphne
    sys.argv = [
        'daphne',
        '-b', '0.0.0.0',
        '-p', '8000',
        '-v', '2',
        'ecommerce_platform.asgi:application'
    ]
    
    CommandLineInterface().run()
