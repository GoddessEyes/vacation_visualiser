"""Основные роуты приложения."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, URLPattern
from typing import List

admin.site.site_header = 'Администрирование Vacation Visualiser'
admin.site.site_title = 'Vacation Visualiser'

urlpatterns: List[URLPattern] = [
    path('admin/', admin.site.urls),
    path('api/', include('vacation_visualiser.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT,
    )
