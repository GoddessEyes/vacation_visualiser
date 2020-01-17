"""Базовые настроки django app."""

from django.apps import AppConfig


class VacationHistoryConfig(AppConfig):
    """Конфигурация vacation_history."""

    name: str = 'vacation_visualiser.api.vacation_history'
    verbose_name: str = 'История отпусков'
