"""Serializer`s моделей модуля `Сотрудники`."""

from rest_framework import serializers, exceptions
from vacation_visualiser.api.employee.models import Employee, Position
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _


class PositionSerializer(serializers.ModelSerializer):
    """Serializer `Должности`."""

    class Meta:
        model: Position = Position
        fields: tuple = ('id', 'name')


class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer `Сотрудника`."""

    position: PositionSerializer = PositionSerializer()

    class Meta:
        model: Employee = Employee
        fields: tuple = (
            'id',
            'username',
            'middle_name',
            'first_name',
            'last_name',
            'position',
        )


UserModel = get_user_model()


class CustomLoginSerializer(serializers.Serializer):
    username: str = serializers.CharField(required=False, allow_blank=False)
    password: str = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username: str = attrs.get('username')
        password: str = attrs.get('password')

        user: str = self._validate_username(username, password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        attrs['user'] = user
        return attrs
