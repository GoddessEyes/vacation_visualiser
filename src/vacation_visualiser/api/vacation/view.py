"""View`s модуля `Отпуска`."""

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from vacation_visualiser.api.vacation.models import Vacation
from vacation_visualiser.api.vacation.serializers import VacationSerializer


class VacationView(ReadOnlyModelViewSet):
    """View графика `Отпусков`."""

    serializer_class = VacationSerializer
    queryset = Vacation.objects.all()
    permission_classes = (IsAuthenticated, )
