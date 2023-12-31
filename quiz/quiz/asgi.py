"""
ASGI config for quiz project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')

application = get_asgi_application()
