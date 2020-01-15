from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils.text import slugify
from openpyxl import load_workbook
import os
from vacation_visualiser.api.employee.models import Employee
from transliterate import translit
import logging


class Command(BaseCommand):

    logging.basicConfig(
        filename='import_employees_log.txt',
        level=logging.INFO,
    )

    def handle(self, *args, **options):
        wb = load_workbook(
            os.path.dirname(os.path.abspath(__file__)) + '/employees.xlsx'
        ).active

        for item in (item[0].value for item in wb.iter_rows()):
            try:
                last_name, first_name, middle_name = item.split()
            except AttributeError as err:
                logging.info(
                    f'Ошибка импорта: {item}, возможно пустая строка.\n'
                    f'Текст ошибки: {err} \n'
                )
                continue
            except ValueError as err:
                logging.info(
                    f'Ошибка импорта: {item}, возможно не полное ФИО.\n'
                    f'Текст ошибки: {err} \n'
                )
                continue
            try:
                Employee(
                    username=slugify(
                        translit(
                            f'{last_name} {first_name}',
                            'ru',
                            reversed=True,
                        )
                    ),
                    first_name=first_name,
                    last_name=last_name,
                    middle_name=middle_name,
                    password=last_name,
                ).save()
            except IntegrityError as err:
                logging.info(
                    f'Ошибка импорта: {last_name, first_name, middle_name}. \n'
                    f'Возможно сотрудник уже существует. \n'
                    f'Текст ошибки: {err} \n'
                )
