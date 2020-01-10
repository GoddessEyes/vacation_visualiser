"""Prod настройки приложения."""

from .base import *


DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'vacation_visualiser'),
        'USER': os.getenv('POSTGRES_USER', 'vacation_visualiser'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'vacation_visualiser'),
        'HOST': os.getenv('POSTGRES_HOST', 'postgres'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    },
}
