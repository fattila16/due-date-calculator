import abc


class DueDateStrategyAbstract():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def calculate_due_date(self, submit_date, turnaround_hours):
        """ Required Method """
        raise NotImplementedError
