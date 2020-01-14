from typing import Tuple

from rest_framework import serializers

from vacation_visualiser.api.vacation.models import Vacation


class UserVacationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model: Vacation = Vacation
        fields: Tuple[str, ...] = (
            'id',
            'date_start',
            'date_end',
        )
