"""CP1404/CP5632 Practical 06 – Guitar class.

Estimate: 15 min
Actual: 13min
"""

CURRENT_YEAR = 2025


class Guitar:
    """Represent a Guitar."""

    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0) -> None:
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self) -> int:
        return CURRENT_YEAR - self.year

    def is_vintage(self) -> bool:
        return self.get_age() >= 50

    def __str__(self) -> str:
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
