"""Модели описывающие график отпусков."""

from django.db import models


class Vacation(models.Model):
    """Модель `Отпуск` - в совокупности описывает график отпусков."""

    date_start = models.DateField(
        verbose_name='Дата начала отпуска',
    )
    date_end = models.DateField(
        verbose_name='Дата окончания отпуска',
    )
    employee = models.ForeignKey(
        verbose_name='Сотрудник',
        to='employee.Employee',
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return (
            f'{self.employee.middle_name} {self.employee.first_name} - '
            f'Начало: {self.date_start} / Окончание: {self.date_end}'
        )

    class Meta:
        verbose_name = 'Отпуск'
        verbose_name_plural = 'Отпуска'
