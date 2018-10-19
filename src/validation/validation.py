import datetime as dt
import math


class Validation():
    @staticmethod
    def is_valid_date(date):
        return isinstance(date, dt.datetime)

    @staticmethod
    def is_valid_turnaround_hours(t_hours):
        if isinstance(t_hours, str) or t_hours < 0 or math.isnan(t_hours):
            return False
        return True

    @staticmethod
    def time_out_of_range(date, _range):
        hours = date.hour + date.minute/60 + date.second/3600
        if hours < _range[0] or hours > _range[1]:
            return False
        return True

    @staticmethod
    def is_date_on_weekday(date):
        if date.weekday() >= 0 and date.weekday() < 5:
            return True
        return False
