"""Модуль настроек админ-панели `Vacation`."""

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from django.db.transaction import atomic
from django.forms.models import ModelFormMetaclass
from vacation_visualiser.api.vacation.create_history_model_helpers import (
    create_history_model,
)
from vacation_visualiser.api.vacation.models import Vacation


@admin.register(Vacation)
class VacationAdmin(admin.ModelAdmin):
    """Админ-класс отображения модели `Отпуска`."""

    @atomic
    def save_model(
        self, request: WSGIRequest, obj: Vacation, form: ModelFormMetaclass, change: bool,
    ) -> None:
        """Создает, лиюо обновляет инстанс Vacation, а также создает VacationHistory."""
        if change:
            create_history_model(Vacation.objects.get(id=obj.id))

        super().save_model(request, obj, form, change)
