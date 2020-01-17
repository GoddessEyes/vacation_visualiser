"""View`s модуля `Отпуска`."""

from typing import List, Tuple

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from vacation_visualiser.api.vacation.filters import VacationFilterSet
from vacation_visualiser.api.vacation.models import Vacation
from vacation_visualiser.api.vacation.serializers import VacationSerializer


class VacationView(ReadOnlyModelViewSet):
    """View API графика `Отпусков`."""

    serializer_class: VacationSerializer = VacationSerializer
    queryset: List[Vacation] = Vacation.objects.all()
    permission_classes: Tuple[object, ...] = (IsAuthenticated, )
    filter_backends: Tuple[object, ...] = (DjangoFilterBackend, )
    filter_class = VacationFilterSet
