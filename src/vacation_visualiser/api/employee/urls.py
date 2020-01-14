"""Роуты модуля `Сотрудники`."""

from rest_framework.routers import DefaultRouter
from vacation_visualiser.api.employee.views import (
    EmployeeView, PositionView, DepartmentView
)

router = DefaultRouter()

router.register(r'employee', EmployeeView)
router.register(r'position', PositionView)
router.register(r'department', DepartmentView)
