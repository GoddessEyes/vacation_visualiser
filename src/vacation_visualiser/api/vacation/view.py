"""View`s модуля `Отпуска`."""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from vacation_visualiser.api.vacation.models import Vacation
from vacation_visualiser.api.vacation.serializers import VacationSerializer
from typing import List, Tuple


class VacationView(ReadOnlyModelViewSet):
    """View API графика `Отпусков`."""

    serializer_class: 'VacationSerializer' = VacationSerializer
    queryset: 'List[Vacation]' = Vacation.objects.all()
    permission_classes: 'Tuple[object, ...]' = (IsAuthenticated, )

