"""Serializer`s модуля `Отпуска`."""

from rest_framework import serializers
from vacation_visualiser.api.employee.serializers import EmployeeSerializer
from vacation_visualiser.api.vacation.models import Vacation


class VacationSerializer(serializers.ModelSerializer):
    """Serializer модели `Vacation`."""

    employee = EmployeeSerializer()

    class Meta:
        model = Vacation
        fields = ('employee', 'date_start', 'date_end')
