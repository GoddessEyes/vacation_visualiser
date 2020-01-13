"""Serializer`s модуля `Отпуска`."""

from rest_framework import serializers
from vacation_visualiser.api.employee.serializers import EmployeeSerializer
from vacation_visualiser.api.vacation.models import Vacation


class VacationSerializer(serializers.ModelSerializer):
    """Serializer модели `Vacation`."""

    employee: EmployeeSerializer = EmployeeSerializer()

    class Meta:
        model: Vacation = Vacation
        fields: tuple = ('employee', 'date_start', 'date_end')
