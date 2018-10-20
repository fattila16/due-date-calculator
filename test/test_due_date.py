import datetime as dt
from unittest import TestCase

from src.models.due_date import DueDate


class TestDueDate(TestCase):
    def setUp(self):
        self.due_date = DueDate(9, 17, None)

    def test_due_date_class(self):
        self.assertIsInstance(self.due_date, DueDate)
    
    def test_calulcate_due_date(self):
        test_date = dt.datetime(2018, 10, 22, 13, 20,0)
        test_turnaround_hours = 6
        result = self.due_date.calculate_due_date(test_date, test_turnaround_hours)
        self.assertEqual(dt.datetime(2018, 10, 23, 11, 30), result)
