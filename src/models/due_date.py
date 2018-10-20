from src.strategy.emar_due_date_strategy import EmarDueDateStrategy

class DueDate:
    def __init__(self, start_hour, end_hour, strategy):
        self.start_hour = start_hour
        self.end_hour = end_hour
        if not strategy:
            strategy = EmarDueDateStrategy(self.start_hour, self.end_hour)
        self.strategy = strategy

    def calculate_due_date(self, submit_date, turnaround_hours):
        return self.strategy.calculate_due_date(submit_date, turnaround_hours)
