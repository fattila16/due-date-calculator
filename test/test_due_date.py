import datetime as dt
from unittest import TestCase

from src.strategy.emar_due_date_strategy import EmarDueDateStrategy


class TestDueDate(TestCase):
    def setUp(self):
        self.due_date = EmarDueDateStrategy(9, 17)
        self.test_date = dt.datetime(2018, 10, 18, 12, 50)
        self.test_turnaround_hours = 6

    def test_invalid_date_format(self):
        test_date = "2018-10-19 12:50"
        with self.assertRaises(TypeError) as context:
            self.due_date.validate_args(test_date, self.test_turnaround_hours)
        self.assertTrue("Invalid submit. Date should be python datetime." in str(context.exception))

    def test_invalid_turnaround_format(self):
        test_turnaround_hours = "test"
        with self.assertRaises(TypeError) as context:
            self.due_date.validate_args(self.test_date, test_turnaround_hours)
        self.assertTrue("Invalid turnaround hours.\
 It must be a non-negative int." in str(context.exception))

    def test_invalid_times_in_date(self):
        test_date = dt.datetime(2018, 10, 18, 17, 50)
        error_msg = "Invalid date. Time must be between {} and {}".format(
            self.due_date.start_hour, self.due_date.end_hour)
        with self.assertRaises(ValueError) as context:
            self.due_date.validate_args(test_date, self.test_turnaround_hours)
        self.assertTrue(error_msg in str(context.exception))

    def test_is_on_weekday(self):
        test_date = dt.datetime(2018, 10, 20, 13, 20)
        with self.assertRaises(ValueError) as context:
            self.due_date.validate_args(test_date, self.test_turnaround_hours)
        self.assertTrue("Invalid date. The given date is on a weekend." in str(context.exception))

    def test_remaining_hours(self):
        test_date = dt.datetime(2018, 10, 18, 16, 0, 0)
        result = self.due_date.remaining_working_hours_in_sec(test_date)
        self.assertEqual(3600, result)

    def test_next_valid_work_day(self):
        test_date = dt.datetime(2018, 10, 19, 15, 30, 0)
        result = self.due_date.next_valid_work_day(test_date)
        self.assertEqual(dt.datetime(2018, 10, 22, 9, 0, 0), result)

    def test_for_friday_2_days(self):
        test_date = dt.datetime(2018, 10, 18, 15, 30, 0)
        test_turnaround_hours = 16
        result = self.due_date.calculate_due_date(test_date, test_turnaround_hours)
        self.assertEqual(dt.datetime(2018, 10, 22, 15, 30), result)

    def test_for_monday_2_days(self):
        test_date = dt.datetime(2018, 10, 22, 15, 30, 0)
        test_turnaround_hours = 16
        result = self.due_date.calculate_due_date(test_date, test_turnaround_hours)
        self.assertEqual(dt.datetime(2018, 10, 24, 15, 30), result)

    def test_for_same_day(self):
        test_date = dt.datetime(2018, 10, 22, 12, 30, 0)
        test_turnaround_hours = 4
        result = self.due_date.calculate_due_date(test_date, test_turnaround_hours)
        self.assertEqual(dt.datetime(2018, 10, 22, 16, 30), result)

    def test_for_week_long(self):
        test_date = dt.datetime(2018, 10, 22, 9, 30, 0)
        test_turnaround_hours = 40
        result = self.due_date.calculate_due_date(test_date, test_turnaround_hours)
        self.assertEqual(dt.datetime(2018, 10, 29, 9, 30), result)

    def test_add_a_day(self):
        test_date = dt.datetime(2018, 10, 22, 15, 30, 0)
        result = EmarDueDateStrategy.add_days(test_date)
        self.assertEqual(dt.datetime(2018, 10, 23, 15, 30), result)
