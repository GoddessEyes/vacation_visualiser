"""View`s модуля `Сотрудники`."""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from vacation_visualiser.api.employee.models import (
    Employee, Position, Department
)
from vacation_visualiser.api.employee.serializers import (
    EmployeeListSerializer,
    EmployeeRetrieveSerializer,
    PositionSerializer,
    DepartmentSerializer,
)
from typing import List, Tuple
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class EmployeeView(ReadOnlyModelViewSet):
    """View API `Сотрудники`."""

    queryset: 'List[Employee]' = Employee.objects.all()
    permission_classes: 'Tuple[object, ...]' = (IsAuthenticated, )
    filter_backends: Tuple[object, ...] = (DjangoFilterBackend, SearchFilter, )
    filterset_fields = ('position', )
    search_fields = ('first_name', 'middle_name', 'last_name', 'position__name')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EmployeeRetrieveSerializer
        else:
            return EmployeeListSerializer


class PositionView(ReadOnlyModelViewSet):
    """View API `Должность`."""
    queryset: 'List[Position]' = Position.objects.all()
    permission_classes: 'Tuple[object, ...]' = (IsAuthenticated, )
    serializer_class = PositionSerializer
    filter_backends: Tuple[object, ...] = (DjangoFilterBackend, SearchFilter,)
    filterset_fields = ('name', 'department', )
    search_fields = ('name', )


class DepartmentView(ReadOnlyModelViewSet):
    """View API `Отдел`."""
    queryset: 'List[Department]' = Department.objects.all()
    permission_classes: 'Tuple[object, ...]' = (IsAuthenticated, )
    serializer_class = DepartmentSerializer
