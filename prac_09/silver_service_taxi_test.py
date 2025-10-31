"""
CP1404/CP5632 Practical
Tests for SilverServiceTaxi.
Estimate: 15 min
Actual: 8 min
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Limo", fuel=100, fanciness=2)
    taxi.start_fare()
    taxi.drive(18)

    # Expected (before rounding change in Taxi): 2.46 * 18 + 4.50 = 48.78
    # With rounding to 10c in Taxi.get_fare(): 2.46*18 -> 44.28 -> 44.3; + 4.5 = 48.8
    fare = taxi.get_fare()
    print(taxi)
    print(f"Fare for 18km with fanciness 2 should be about $48.80 -> ${fare:.2f}")
    assert abs(fare - 48.8) < 0.001


if __name__ == "__main__":
    main()
