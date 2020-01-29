"""Модели описывающие график отпусков."""

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

    def __str__(self) -> str:
        return (
            f'{self.employee.middle_name} {self.employee.first_name} - '
            f'Начало: {self.date_start} / Окончание: {self.date_end}'
        )

    class Meta:
        abstract = True


class Vacation(AbstractVacation):
    """Модель `Отпуск` - в совокупности описывает график отпусков."""

    def __str__(self) -> str:
        return (
            f'{self.employee.middle_name} {self.employee.first_name} - '
            f'Начало: {self.date_start} / Окончание: {self.date_end}'
        )

    class Meta:
        verbose_name: str = 'Отпуск'
        verbose_name_plural: str = 'Отпуска'
