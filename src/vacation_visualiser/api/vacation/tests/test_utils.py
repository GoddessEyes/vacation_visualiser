"""Функции используемые в авто-тестах."""

from faker import Faker
from vacation_visualiser.api.vacation.models import Vacation


def change_vacation_dates(vacation: Vacation) -> None:
    """Обновляет модель отпуска случайными датами."""
    faker = Faker()

    vacation.date_start = faker.date_object()
    vacation.date_end = faker.date_between(start_date=faker.date_object())
    vacation.save()
