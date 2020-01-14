"""Модуль настроек админ-панели `Employee`."""
from typing import Tuple, Dict

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from rest_framework.authtoken.models import Token
from vacation_visualiser.api.employee.models import (
    Employee, Position, Department
)
from vacation_visualiser.api.vacation.models import Vacation


admin.site.register(Position)
admin.site.register(Department)


class TokenInline(admin.StackedInline):
    """Админ-элемент `Employee -> Token's`."""

    model: Token = Token
    readonly_fields: Tuple[str, ...] = ('created', )
    can_delete: bool = False
    classes: Tuple[str, ...] = ('collapse',)


class VacationInline(admin.StackedInline):
    """Админ-элемент `Employee -> Vacation's`."""

    model: Vacation = Vacation
    extra = 1


class EmployeeChangeForm(UserChangeForm):
    """Переопределённая форма изменения `Сотрудника`."""

    class Meta:
        model = Employee
        fields = (
            'username',
            'middle_name',
            'first_name',
            'last_name',
        )


class EmployeeCreationForm(UserCreationForm):
    """Переопределённая форма добавления `Сотрудника`."""

    class Meta:
        model = Employee
        fields = (
            'username', 'last_name', 'first_name', 'middle_name', 'password',
        )


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    """Админ-класс отображения модели `Сотрудника`."""

    inlines = (TokenInline, VacationInline)
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm

    list_display: Tuple[str, ...] = (
        'last_name', 'first_name', 'middle_name', 'position'
    )

    prepopulated_fields: Dict[str, Tuple[str, ...]] = {
        'username': (
            'last_name', 'first_name',
        ),
    }

    add_fieldsets: Tuple[Tuple[(None, Dict[str, Tuple[str, ...]])]] = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'last_name',
                    'first_name',
                    'middle_name',
                    'username',
                    'password1',
                    'password2',
                    'position',
                ),
            },
        ),
    )
    fieldsets: Tuple[Tuple[(None, Dict[str, Tuple[str, ...]])]] = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'last_name',
                    'first_name',
                    'middle_name',
                    'username',
                    'position',
                ),
            },
        ),
    )
