"""
CP1404/CP5632 Practical
Taxi class (extends Car)
Student-style version using a class variable for price_per_km and rounding fares to 10c.
Estimate: 15 min
Actual: 12 min
"""
from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""

    # Class variable shared by all taxis (can be overridden per instance if needed)
    price_per_km = 1.23

    def __init__(self, name: str, fuel: float):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self) -> str:
        """Return a string like a Car but with current fare distance and price info."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"

    def get_fare(self) -> float:
        """Return the price for the current fare, rounded to the nearest 10c.

        NOTE: This returns a *number*, not a formatted string.
        """
        return round(self.price_per_km * self.current_fare_distance, 1)

    def start_fare(self) -> None:
        """Begin a new fare (reset the fare distance)."""
        self.current_fare_distance = 0

    def drive(self, distance: float) -> float:
        """Drive like parent Car but also track distance for the fare.

        Returns the distance actually driven (could be less if we run out of fuel).
        """
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
