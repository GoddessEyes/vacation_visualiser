"""Модели связанные с сущностью `Сотрудник`."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    """`Отдел` должности."""

    name: 'models.CharField[str, str]' = models.CharField(
        'Отдел',
        max_length=50,
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name: str = 'Отдел'
        verbose_name_plural: str = 'Отделы'


class Position(models.Model):
    """`Должность` сотрудника."""

    name: 'models.CharField[str, str]' = models.CharField(
        'Должность',
        max_length=50,
    )
    department: 'models.ForeignKey[Department, str]' = models.ForeignKey(
        to=Department,
        verbose_name='Отдел',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'{self.name} Отдел: {self.department or "Отсутствует"}'

    class Meta:
        verbose_name: str = 'Должность'
        verbose_name_plural: str = 'Должности'


class Employee(AbstractUser):
    """`Сотрудник`."""

    first_name: 'models.CharField[str, str]' = models.CharField(
        'Имя',
        max_length=30,
        blank=False,
        null=False,
        help_text='Имя сотрудника',
    )
    last_name: 'models.CharField[str, str]' = models.CharField(
        'Фамилия',
        max_length=30,
        blank=False,
        null=False,
        help_text='Фамилия сотрудника',
    )
    middle_name: 'models.CharField[str, str]' = models.CharField(
        'Отчество',
        max_length=30,
        blank=False,
        null=False,
        help_text='Отчество сотрудника',
    )
    position: 'models.ForeignKey[Position, str]' = models.ForeignKey(
        Position,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.middle_name} {self.last_name}'

    class Meta:
        verbose_name: str = 'Сотрудник'
        verbose_name_plural: str = 'Сотрудники'
