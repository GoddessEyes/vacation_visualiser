"""Serializer`s моделей модуля `Сотрудники`."""
from typing import Tuple

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, serializers
from vacation_visualiser.api.employee.models import (
    Department,
    Employee,
    Position,
)
from vacation_visualiser.api.vacation.import_serializers import (
    UserVacationsListSerializer,
)


class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer `Отдела`."""

    class Meta:
        model: Department = Department
        fields: Tuple[str, ...] = ('id', 'name')


class PositionSerializer(serializers.ModelSerializer):
    """Serializer `Должности`."""

    department: DepartmentSerializer = DepartmentSerializer()

    class Meta:
        model: Position = Position
        fields: Tuple[str, ...] = ('id', 'name', 'department')


class EmployeeListSerializer(serializers.ModelSerializer):
    """Serializer `Сотрудника`."""

    position: PositionSerializer = PositionSerializer()

    class Meta:
        model: Employee = Employee
        fields: Tuple[str, ...] = (
            'id',
            'username',
            'middle_name',
            'first_name',
            'last_name',
            'position',
        )


class EmployeeRetrieveSerializer(serializers.ModelSerializer):
    """Serializer `Сотрудника`."""

    position: PositionSerializer = PositionSerializer()
    vacation_set: UserVacationsListSerializer = UserVacationsListSerializer(
        many=True,
    )

    class Meta:
        model: Employee = Employee
        fields: Tuple[str, ...] = (
            'id',
            'username',
            'last_name',
            'first_name',
            'middle_name',
            'position',
            'vacation_set',
        )


UserModel = get_user_model()


class CustomLoginSerializer(serializers.Serializer):
    """Переопределённый serializer для Auth."""

    username: str = serializers.CharField(required=False, allow_blank=False)
    password: str = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs) -> Employee:
        """Аунтентификация."""
        return authenticate(self.context['request'], **kwargs)

    def _validate_username(self, username, password) -> Employee:
        """Валидация username&password."""
        if username and password:
            user: Employee = self.authenticate(
                username=username,
                password=password,
            )
        else:
            msg = _('Must include "username" and "password".')  # noqa: WPS121
            raise exceptions.ValidationError(msg)

        return user or None

    def validate(self, attrs):
        """Валидация и aутентификация username&password."""
        username: str = attrs.get('username')
        password: str = attrs.get('password')

        user = self._validate_username(username, password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')  # noqa: WPS121
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')  # noqa: WPS121
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs
