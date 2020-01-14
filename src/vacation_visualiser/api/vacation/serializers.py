"""Serializer`s модуля `Отпуска`."""
from typing import Tuple

from rest_framework import serializers
from vacation_visualiser.api.employee.serializers import EmployeeListSerializer
from vacation_visualiser.api.vacation.models import Vacation


class VacationSerializer(serializers.ModelSerializer):
    """Serializer модели `Vacation`."""

    employee: EmployeeListSerializer = EmployeeListSerializer()

    class Meta:
        model: Vacation = Vacation
        fields: Tuple[str, ...] = ('id', 'employee', 'date_start', 'date_end')
