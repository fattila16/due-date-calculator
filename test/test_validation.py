import datetime as dt
from unittest import TestCase

from src.validation.validation import Validation


class TestValidation(TestCase):

    def test_is_valid_date_true(self):
        test_date = dt.datetime(2018, 10, 19, 12, 50)
        self.assertTrue(Validation.is_valid_date(test_date))

    def test_is_valid_date_wrong_fromat(self):
        test_date = "2018-10-18 12:50"
        self.assertFalse(Validation.is_valid_date(test_date))

    def test_date_time_out_of_range_false(self):
        test_date = dt.datetime(2018, 10, 12, 17, 50)
        self.assertFalse(Validation.time_out_of_range(test_date, [9, 17]))

    def test_date_time_out_of_range_true(self):
        test_date = dt.datetime(2018, 10, 12, 17, 0, 0)
        self.assertTrue(Validation.time_out_of_range(test_date, [9, 17]))

    def test_is_valid_turnaround_hours_false(self):
        test_turnaround_hours = [-1, 'test']
        for item in test_turnaround_hours:
            self.assertFalse(Validation.is_valid_turnaround_hours(item))

    def test_is_valid_turnaround_hours_true(self):
        test_turnaround_hours = 5
        self.assertTrue(Validation.is_valid_turnaround_hours(test_turnaround_hours))

    def test_is_date_on_weekday_true(self):
        test_date = dt.datetime(2018, 10, 19, 12, 40)
        self.assertTrue(Validation.is_date_on_weekday(test_date))

    def test_is_date_on_weekday_false(self):
        test_date = dt.datetime(2018, 10, 20, 13, 20)
        self.assertFalse(Validation.is_date_on_weekday(test_date))
