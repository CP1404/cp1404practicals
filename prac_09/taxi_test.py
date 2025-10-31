"""
CP1404/CP5632 Practical
Simple tests/client code for Taxi class.
Estimate: 15 min
Actual: 7 min
"""
from taxi import Taxi


def main():
    # 1. create a taxi: name "Prius 1", fuel 100 (price uses class variable)
    my_taxi = Taxi("Prius 1", 100)

    # 2. drive 40 km
    my_taxi.drive(40)

    # 3. print taxi details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # 4. restart the meter and then drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # 5. print details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
