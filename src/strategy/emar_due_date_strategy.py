import datetime as dt

from src.strategy.due_date_strategy_abstract import DueDateStrategyAbstract
from src.validation.validation import Validation


class EmarDueDateStrategy(DueDateStrategyAbstract):
    def __init__(self, validation, start_hour, end_hour):
        self.start_hour = start_hour
        self.end_hour = end_hour
        if not validation:
            validation = Validation()
        self.validation = validation

    def validate_args(self, submit_date, turnaround_hours):
        if not self.validation.is_valid_date(submit_date):
            raise TypeError("Invalid submit. Date should be python datetime.")

        if not self.validation.is_valid_turnaround_hours(turnaround_hours):
            raise TypeError("Invalid turnaround hours. It must be a non-negative int.")

        if not self.validation.time_out_of_range(submit_date, [self.start_hour, self.end_hour]):
            error_msg = "Invalid date.\
 Time must be between {} and {}".format(self.start_hour, self.end_hour)
            raise ValueError(error_msg)
        if not self.validation.is_date_on_weekday(submit_date):
            raise ValueError("Invalid date. The given date is on a weekend.")

    def remaining_working_hours(self, date):
        day = dt.datetime(date.year, date.month, date.day, self.end_hour, 0, 0)
        diff = day - date
        return diff.total_seconds()

    def add_days(self, date, days):
        temp_date = date
        while days:
            temp_date += dt.timedelta(days=1)
            if self.validation.is_date_on_weekday(temp_date):
                days -= 1
        return temp_date

    def next_valid_work_day(self, date):
        new_date = self.add_days(date, 1)
        return dt.datetime(new_date.year, new_date.month, new_date.day, self.start_hour, 0, 0)

    def calculate_due_date(self, submit_date, turnaround_hours):
        self.validate_args(submit_date, turnaround_hours)

        turnaround_hours_in_sec = turnaround_hours * 3600
        due_date = submit_date

        while turnaround_hours_in_sec > 0:
            remaining_time = self.remaining_working_hours(due_date)
            if remaining_time > turnaround_hours_in_sec:
                due_date += dt.timedelta(seconds=turnaround_hours_in_sec)
                turnaround_hours_in_sec -= turnaround_hours_in_sec
            else:
                due_date += dt.timedelta(seconds=remaining_time)
                turnaround_hours_in_sec -= remaining_time

            if turnaround_hours_in_sec > 0:
                due_date = self.next_valid_work_day(due_date)
        return due_date
