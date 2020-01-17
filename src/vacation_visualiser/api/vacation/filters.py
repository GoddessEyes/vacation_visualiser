"""Кастомные фильтры модуля `Отпуска`."""

from django_filters import BaseInFilter, FilterSet, NumberFilter
from vacation_visualiser.api.vacation.models import Vacation


class VacationFilterSet(FilterSet):
    """Фильтры `последовательность id сотрудников` и `Отдел`."""

    employee_id__in = BaseInFilter(  # noqa: WPS116
        field_name='employee_id', lookup_expr='in',
    )
    employee__position__department = NumberFilter(  # noqa: WPS116
        field_name='employee__position__department',
    )

    class Meta:
        model = Vacation
        fields = ('employee_id__in', 'employee__position__department')
