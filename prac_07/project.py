"""
CP1404/CP5632 Practical 07 - Project class for the Project Management program.
Estimate: 15 min
Actual: 10 min
"""
from datetime import date

class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        return f"<Project {self.name}, priority={self.priority}, completion={self.completion_percentage}%>"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.completion_percentage == 100
