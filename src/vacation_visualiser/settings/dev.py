"""Dev настройки приложения."""
import dj_database_url

from .base import *
import os

DATABASE_URL = os.getenv('DATABASE_URL', False)

if DATABASE_URL:
    DATABASES['default'] = dj_database_url.config(
        default=DATABASE_URL
    )
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'vacation_visualiser.sqlite3'),
        },
    }
DEBUG = True
