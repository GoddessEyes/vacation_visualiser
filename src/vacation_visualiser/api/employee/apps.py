"""Модуль `Персонал`."""

from django.apps import AppConfig


class EmployeeConfig(AppConfig):
    """Конфигурация `app Employee`."""

    name = 'vacation_visualiser.api.employee'
    verbose_name = 'Персонал'
