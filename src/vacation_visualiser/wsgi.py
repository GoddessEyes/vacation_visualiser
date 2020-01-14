"""WSGI config for vacation_visualiser project."""

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.vacation_visualiser.settings.dev')

application = get_wsgi_application()
