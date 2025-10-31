"""CP1404/CP5632 Practical 06 – Client code to use the Car class.

Estimate: 10 min
Actual: 6 min
"""

from prac_06.car import Car


def main() -> None:
    """Demo test code to show how to use Car class (now with names)."""
    # Existing demo car
    my_car = Car("Demo Car", 180)
    my_car.drive(30)


    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Limo fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)


if __name__ == "__main__":
    main()
