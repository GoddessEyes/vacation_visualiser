"""View`s модуля `Сотрудники`."""

from typing import List, Tuple

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from vacation_visualiser.api.employee.models import (
    Department,
    Employee,
    Position,
)
from vacation_visualiser.api.employee.serializers import (
    DepartmentSerializer,
    EmployeeListSerializer,
    EmployeeRetrieveSerializer,
    PositionSerializer,
)


class EmployeeView(ReadOnlyModelViewSet):
    """View API `Сотрудники`."""

    queryset: List[Employee] = Employee.objects.all().order_by('last_name')
    permission_classes: Tuple[object, ...] = (IsAuthenticated, )
    filter_backends: Tuple[object, ...] = (DjangoFilterBackend, SearchFilter)
    filterset_fields: Tuple[str, ...] = ('position', 'position__department')
    search_fields: Tuple[str, ...] = (
        'first_name',
        'middle_name',
        'last_name',
        'position__name',
    )

    def get_serializer_class(self):
        """Возвращает разные serializer`s для list/retrieve запросов."""
        if self.action == 'retrieve':
            return EmployeeRetrieveSerializer
        return EmployeeListSerializer


class PositionView(ReadOnlyModelViewSet):
    """View API `Должность`."""

    queryset: List[Position] = Position.objects.all()
    permission_classes: Tuple[object, ...] = (IsAuthenticated, )
    serializer_class = PositionSerializer
    filter_backends: Tuple[object, ...] = (DjangoFilterBackend, )
    filterset_fields = ('name', 'department')


class DepartmentView(ReadOnlyModelViewSet):
    """View API `Отдел`."""

    queryset: 'List[Department]' = Department.objects.all()
    permission_classes: 'Tuple[object, ...]' = (IsAuthenticated, )
    serializer_class = DepartmentSerializer
