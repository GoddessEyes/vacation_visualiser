"""Модуль настроек админ-панели `Employee`."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from rest_framework.authtoken.models import Token
from vacation_visualiser.api.employee.models import Employee, Position
from vacation_visualiser.api.vacation.models import Vacation


admin.site.register(Position)


class TokenInline(admin.StackedInline):
    """Админ-элемент `Employee -> Token's`."""

    model = Token
    readonly_fields = ('created',)
    can_delete = False
    classes = ('collapse',)


class VacationInline(admin.StackedInline):
    """Админ-элемент `Employee -> Vacation's`."""

    model = Vacation
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
            'username', 'middle_name', 'first_name', 'last_name', 'password',
        )


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    """Админ-класс отображения модели `Сотрудника`."""

    inlines = (TokenInline, VacationInline)
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm

    list_display = ('username', 'middle_name', 'first_name', 'position')

    prepopulated_fields = {
        'username': (
            'middle_name', 'first_name',
        ),
    }

    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'middle_name',
                    'first_name',
                    'last_name',
                    'username',
                    'password1',
                    'password2',
                    'position',
                ),
            },
        ),
    )
    fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'middle_name',
                    'first_name',
                    'last_name',
                    'username',
                    'position',
                ),
            },
        ),
    )
