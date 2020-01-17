"""Модели описывающие историю отпусков."""

from django.db import models
from vacation_visualiser.api.vacation.models import AbstractVacation, Vacation


class VacationHistory(AbstractVacation):
    """Отображает исотрию изменений отпусков пользователя."""

    previous: 'models.OneToOneField[models.Model, str]' = models.OneToOneField(
        verbose_name='Предыдущий отпуск',
        to='self',
        null=True,
        on_delete=models.PROTECT,
    )

    actual: 'models.ForeignKey[models.Model, str]' = models.ForeignKey(
        verbose_name='Активный отпуск',
        to=Vacation,
        on_delete=models.PROTECT,
        null=False,
        related_name='history_vacations',
    )

    def __str__(self) -> str:
        return f'Перенесенный отпуск сотрудника {self.actual_vacation.employee}'

    class Meta:
        verbose_name: str = 'Перенесенный отпуск'
        verbose_name_plural: str = 'Переносы отпусков'
