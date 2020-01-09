from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from rest_framework.authtoken.models import Token

from vacation_visualiser.api.employee.models import Employee, Position


admin.site.register(Position)


class TokenInline(admin.StackedInline):
    model = Token
    readonly_fields = ('created',)
    can_delete = False
    classes = ('collapse',)


class EmployeeChangeForm(UserChangeForm):

    class Meta:
        model = Employee
        fields = ('username', 'middle_name', 'first_name', 'last_name', )


class EmployeeCreationForm(UserCreationForm):

    class Meta:
        model = Employee
        fields = (
            'username', 'middle_name', 'first_name', 'last_name', 'password'
        )


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    inlines = (TokenInline, )
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm

    list_display = ('username', 'middle_name', 'first_name', 'position')

    prepopulated_fields = {'username': ('middle_name', 'first_name', )}

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
            }
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
            }
        ),
    )
