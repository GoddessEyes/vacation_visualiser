"""Функции отвечающие за содание инстанса VacationHistory."""

from datetime import date
from typing import Dict, Union

from vacation_visualiser.api.vacation.models import Vacation
from vacation_visualiser.api.vacation_history.models import VacationHistory


def create_history_model(vacation_model: Vacation) -> VacationHistory:
    """Создает инстанс VacationHistory."""
    previous_history_query = VacationHistory.objects.filter(
        actual=vacation_model, next__isnull=True,
    )

    previous_history = previous_history_query.first()
    history_model = VacationHistory.objects.create(
        **prepare_create_history_model_args(vacation_model, previous_history),
    )

    previous_history_query.exclude(id=history_model.id).update(next=history_model)
    return history_model


def prepare_create_history_model_args(
    vacation_model: Vacation, previous_history_model: VacationHistory,
) -> Dict[str, Union[date, date, int, Vacation, VacationHistory]]:
    """Форматирует данные для создания VacationHistory."""
    return {
        **vacation_to_dict(vacation_model),
        **{
            'actual': vacation_model,
            'previous': previous_history_model,
        },
    }


def vacation_to_dict(vacation_model: Vacation) -> Dict[str, Union[date, date, int]]:
    """Приводит инстанс Vacation к дикту с необходимыми ключами."""
    return {
        'date_start': vacation_model.date_start,
        'date_end': vacation_model.date_end,
        'employee_id': vacation_model.employee_id,
    }
