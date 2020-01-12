"""Модели связанные с сущностью `Сотрудник`."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    """`Должность` сотрудника."""

    name = models.CharField(
        'Должность',
        max_length=50,
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(AbstractUser):
    """`Сотрудник`."""

    first_name = models.CharField(
        'Имя',
        max_length=30,
        blank=False,
        null=False,
        help_text='Имя сотрудника',
    )
    middle_name = models.CharField(
        'Фамилия',
        max_length=30,
        blank=False,
        null=False,
        help_text='Фамилия сотрудника',
    )
    last_name = models.CharField(
        'Отчество',
        max_length=30,
        blank=False,
        null=False,
        help_text='Отчество сотрудника',
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'{self.middle_name} {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
