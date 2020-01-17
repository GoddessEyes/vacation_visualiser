"""Роутинг ресурса."""

from rest_framework.routers import DefaultRouter
from vacation_visualiser.api.vacation.view import VacationView


router: DefaultRouter = DefaultRouter()

router.register(r'vacation', VacationView)
