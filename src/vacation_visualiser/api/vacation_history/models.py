"""Модели описывающие историю отпусков."""
from typing import Any

from django.db import models
from vacation_visualiser.api.vacation.models import AbstractVacation, Vacation


class VacationHistory(AbstractVacation):
    """Отображает исотрию изменений отпусков пользователя."""

    next: Any = models.OneToOneField(
        verbose_name='Последующий перенос отпуска',
        to='self',
        null=True,
        on_delete=models.CASCADE,
        related_name='next_vacation',
    )

    previous: Any = models.OneToOneField(
        verbose_name='Предыдущий перенос отпуска',
        to='self',
        null=True,
        on_delete=models.SET_NULL,
        related_name='previous_vacation',
    )

    actual: Any = models.ForeignKey(
        verbose_name='Активный отпуск',
        to=Vacation,
        on_delete=models.CASCADE,
        null=False,
        related_name='history_vacations',
    )

    def __str__(self) -> str:
        return f'Перенесенный отпуск сотрудника {self.actual.employee}'

    class Meta:
        verbose_name: str = 'Перенесенный отпуск'
        verbose_name_plural: str = 'Переносы отпусков'
