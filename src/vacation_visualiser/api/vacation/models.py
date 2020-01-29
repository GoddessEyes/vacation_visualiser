"""Модели описывающие график отпусков."""
from typing import Optional, Union, Sequence

from django.db import models
from vacation_visualiser.api.employee.models import Employee


class AbstractVacation(models.Model):
    """Описывает базовую модель отпуска."""

    date_start: 'models.DateField[str, str]' = models.DateField(
        verbose_name='Дата начала отпуска',
    )
    date_end: 'models.DateField[str, str]' = models.DateField(
        verbose_name='Дата окончания отпуска',
    )
    employee: 'Employee' = models.ForeignKey(
        verbose_name='Сотрудник',
        to=Employee,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class Vacation(AbstractVacation):
    """Модель `Отпуск` - в совокупности описывает график отпусков."""

    def save(
        self,
        force_insert: bool = ...,
        force_update: bool = ...,
        using: Optional[str] = ...,
        update_fields: Optional[Union[Sequence[str], str]] = ...,
    ) -> None:
        timedelta = self.date_end - self.date_start
        self.employee.rest_of_vacation = (
                self.employee.rest_of_vacation - timedelta.days
        )
        self.employee.save()
        super().save()

    def __str__(self) -> str:
        return (
            f'{self.employee.middle_name} {self.employee.first_name} - '
            f'Начало: {self.date_start} / Окончание: {self.date_end}'
        )

    class Meta:
        verbose_name: str = 'Отпуск'
        verbose_name_plural: str = 'Отпуска'
