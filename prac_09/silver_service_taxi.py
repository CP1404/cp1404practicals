"""
CP1404/CP5632 Practical
SilverServiceTaxi - inherits from Taxi, adds fanciness and flagfall.
Estimate: 15 min
Actual: 20 min
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness multiplier and a flagfall charge."""

    flagfall = 4.50

    def __init__(self, name: str, fuel: float, fanciness: float):
        """Construct a SilverServiceTaxi with a fanciness multiplier."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Start from the base class-variable price, then customise per instance
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self) -> str:
        """Show Taxi string plus flagfall information."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self) -> float:
        """Return the total fare = rounded distance fare + flagfall."""
        # Use the parent's rounding behaviour for the distance component
        return super().get_fare() + self.flagfall
