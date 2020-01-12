"""Модуль настроек админ-панели `Vacation`."""

from django.contrib import admin
from vacation_visualiser.api.vacation.models import Vacation


@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    """Админ-класс отображения модели `Отпуска`."""

    list_display = ('employee', 'date_start', 'date_end')
