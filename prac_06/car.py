"""CP1404/CP5632 Practical 06 – Car class example with name.

Estimate: 15 min
Actual: 14 min
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name: str = "Car", fuel: float = 0):
        """Initialise a Car instance.

        name: car's descriptive name
        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0


    def __str__(self) -> str:  # noqa: DunderStr
        """Return string representation"""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount: float) -> None:
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance: float) -> float:
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out. Return the distance actually driven.
        """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            distance_driven = distance
            self.fuel -= distance
        self._odometer += distance_driven
        return distance_driven
