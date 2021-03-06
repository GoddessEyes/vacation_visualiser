"""Конфигурация django admin."""

from django.contrib import admin
from vacation_visualiser.api.vacation_history.models import VacationHistory


@admin.register(VacationHistory)
class VacationHistoryAdmin(admin.ModelAdmin):
    """Класс конфигурации Истории отпусков для админ панели."""
