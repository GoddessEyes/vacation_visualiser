from django.forms import model_to_dict
from django.test import TestCase
from vacation_visualiser.api.vacation.create_history_model_helpers import (
    create_history_model,
)
from vacation_visualiser.api.vacation.models import Vacation
from vacation_visualiser.api.vacation.tests.test_utils import (
    change_vacation_dates,
)
from vacation_visualiser.api.vacation_history.models import VacationHistory


class TestVacationFirstHistory(TestCase):

    fixtures = ('vacation',)

    def test(self):
        vacation = Vacation.objects.first()
        create_history_model(vacation)
        vacation_history = VacationHistory.objects.first()

        self.assertEqual(vacation.date_start, vacation_history.date_start)
        self.assertEqual(vacation.date_end, vacation_history.date_end)
        self.assertEqual(vacation.employee, vacation_history.employee)
        self.assertEqual(vacation, vacation_history.actual)
        self.assertIsNone(vacation_history.next)


class TestVacationMultipleHistory(TestCase):

    fixtures = ('vacation',)

    def setUp(self):

        self.vacation = Vacation.objects.first()
        self.first_vacation_data = model_to_dict(self.vacation)
        self.first_history_model = create_history_model(self.vacation)
        change_vacation_dates(self.vacation)
        self.second_history_model = None
        self.second_vacation_data = None

    def test(self):

        self.assertEqual(
            self.first_vacation_data['date_start'],
            self.first_history_model.date_start,
            'Дата начала отпуска в VacationHistory должна совпадать c Vacation',
        )

        self.assertEqual(
            self.first_vacation_data['date_end'],
            self.first_history_model.date_end,
            'Дата окончания отпуска в VacationHistory должна совпадать с Vacation',
        )

        self.assertIsNone(
            self.first_history_model.next,
            'У последней записи VacationHistory поле next должно быть пустым',
        )

        self.assertEqual(
            self.vacation,
            self.first_history_model.actual,
            'Запись VacationHistory должна ссылаться на инстанс Vacation',
        )

        self.second_vacation_data = model_to_dict(self.vacation)
        self.second_history_model = create_history_model(self.vacation)
        self.first_history_model.refresh_from_db()
        change_vacation_dates(self.vacation)

        self.assertEqual(
            self.second_vacation_data['date_start'],
            self.second_history_model.date_start,
            'Дата начала отпуска в VacationHistory должна совпадать c Vacation',
        )

        self.assertEqual(
            self.second_vacation_data['date_end'],
            self.second_history_model.date_end,
            'Дата окончания отпуска в VacationHistory должна совпадать с Vacation',
        )

        self.assertEqual(
            self.first_history_model,
            self.second_history_model.previous,
            'Все инстансы VacationHistory, кроме первого должны ссылаться на предыдущую запись',
        )

        self.assertEqual(
            self.second_history_model,
            self.first_history_model.next,
            'Все инстансы VacationHistory, кроме последнего должны ссылаться на следующую запись',
        )
