"""Serializer`s для внешних `app`. FIX: cross-import."""

from typing import Tuple

from rest_framework import serializers
from vacation_visualiser.api.vacation.models import Vacation
from vacation_visualiser.api.vacation_history.serializers import (
    VacationHistorySerializer,
)


class UserVacationsListSerializer(serializers.ModelSerializer):
    """Serializer для последовательности `Отпуска Юзера`."""

    history_vacations = VacationHistorySerializer(many=True)

    class Meta:
        model: Vacation = Vacation
        fields: Tuple[str, ...] = (
            'id',
            'date_start',
            'date_end',
            'history_vacations',
        )
