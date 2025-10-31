"""
CP1404/CP5632 Practical
Basic tests for UnreliableCar.
(not strict unit tests due to randomness; these just demonstrate behaviour)
Estimate: 15 min
Actual: 7 min
"""
import random
from unreliable_car import UnreliableCar


def main():
    random.seed(0)  # set a seed so this is repeatable for demonstration

    # Very reliable car should usually drive
    reliable = UnreliableCar("Reliable", fuel=1000, reliability=90.0)
    # Very unreliable car should usually not drive
    unreliable = UnreliableCar("Unreliable", fuel=1000, reliability=10.0)

    # Try many short trips so we can see the effect
    attempts = 100
    distance_each = 1

    for _ in range(attempts):
        reliable.drive(distance_each)
        unreliable.drive(distance_each)

    print(f"Reliable odometer after {attempts} x {distance_each}km: {reliable.odometer}")
    print(f"Unreliable odometer after {attempts} x {distance_each}km: {unreliable.odometer}")

    # Some simple sanity assertions
    assert reliable.odometer > unreliable.odometer
    assert 0 <= unreliable.odometer <= attempts
    assert 0 <= reliable.odometer <= attempts


if __name__ == "__main__":
    main()
