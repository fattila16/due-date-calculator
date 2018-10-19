import datetime as dt
from src.models.due_date import DueDate


def main():
    due_date = DueDate(9, 17, None)
    result = due_date.calculate_due_date(dt.datetime(2018, 10, 22, 14, 20), 4)
    print(result)

if __name__ == "__main__":
    main()
