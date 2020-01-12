"""Dev настройки приложения."""
import dj_database_url

from .base import *
import os

DATABASE_URL = os.getenv('DATABASE_URL', False)

if DATABASE_URL:
    DATABASES['default'] = dj_database_url.config(
        default=DATABASE_URL
    )

DEBUG = True
