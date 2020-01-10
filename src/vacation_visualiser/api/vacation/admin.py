"""Модуль настроек админ-панели `Vacation`."""

from django.contrib import admin
from vacation_visualiser.api.vacation.models import Vacation


admin.site.register(Vacation)
