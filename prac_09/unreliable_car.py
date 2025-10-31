"""
CP1404/CP5632 Practical
UnreliableCar - inherits from Car and sometimes fails to drive.
Estimate: 15 min
Actual: 7 min
"""
import random
from car import Car


class UnreliableCar(Car):
    """Car that only drives based on a reliability percentage (0-100)."""

    def __init__(self, name: str, fuel: float, reliability: float):
        """Construct an UnreliableCar with given reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance: float) -> float:
        """Attempt to drive the given distance based on reliability.

        Returns the distance actually driven (0 if it failed).
        """
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            # Drive like a normal car
            return super().drive(distance)
        # Failed to drive; do not change fuel/odometer
        return 0.0
