# Calculate Due Date

Due date service for Emarsys
## Installiation
To use this service, you need to install python, and pip. The program was written in python3.

First initiate `pip3 install -r requirements.txt`.
The only requirement is nose2 and its peer dependencies. This lib is for testing purposes.

## Usage
If you want to try it out, run `python3 main.py` in the root of the repo.

- You make an instance of the DueDate class, with the start and end hour of your workplace.
- The third attr in the constructor is None because there's only one strategy to use, the default one is the emar_strategy.
- You call the calculate_due_date function with two parameters
- The first one is the submit date, the second is the turnaround hours
- The date must be a python datetime, and the second one is a non-negative int.
- It will calculate you the due date of the ticket.
```
def  main():

due_date = DueDate(9, 17, None)

result = due_date.calculate_due_date(dt.datetime(2018, 10, 22, 14, 20), 4)

print(result)
```

## Background info
I tried to develop the service using strategy design pattern, and in tdd.

## Testing
The test coverage is 95%.
The tests can be run via `nose2` at the root folder. If you don't want to install that lib, use 
`python3 -m unittest discover`
