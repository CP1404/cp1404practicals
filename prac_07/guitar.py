"""
CP1404/CP5632 Practical 07 - Guitar class for the More Guitars program.
Estimate: 10 min
Actual: 9 min
"""
from datetime import datetime

VINTAGE_AGE = 50

class Guitar:

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self):
        return str(self)

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year
