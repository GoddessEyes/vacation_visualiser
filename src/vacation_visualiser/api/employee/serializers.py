"""Serializer`s моделей модуля `Сотрудники`."""

from rest_framework import serializers
from vacation_visualiser.api.employee.models import Employee, Position


class PositionSerializer(serializers.ModelSerializer):
    """Serializer `Должности`."""

    class Meta:
        model = Position
        fields = ('id', 'name')


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer `Сотрудника`."""

    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = (
            'id',
            'username',
            'middle_name',
            'first_name',
            'last_name',
            'position',
        )
