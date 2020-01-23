from typing import Tuple

from rest_framework import serializers
from vacation_visualiser.api.vacation_history.models import VacationHistory


class VacationHistorySerializer(serializers.ModelSerializer):
    """Сериализатор модели VacationHistory."""
    class Meta:
        model: VacationHistory = VacationHistory
        fields: Tuple[str, ...] = ('id', 'date_start', 'date_end', 'next', 'previous', 'actual')
