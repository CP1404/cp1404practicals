"""
CP1404/CP5632 Practical
Taxi simulator using Taxi and SilverServiceTaxi classes.
Estimate: 15 min
Actual: 15 min
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


MENU = """Let's drive!
q)uit, c)hoose taxi, d)rive
>>> """


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
    except ValueError:
        print("Invalid taxi choice")
        return None
    if 0 <= choice < len(taxis):
        return taxis[choice]
    print("Invalid taxi choice")
    return None


def drive_taxi(current_taxi):
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0.0
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0.0
    # Start a new fare for each drive
    current_taxi.start_fare()
    current_taxi.drive(distance)
    fare = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
    return fare


def main():
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, fanciness=2),
        SilverServiceTaxi("Hummer", 200, fanciness=4),
    ]

    bill_to_date = 0.0
    current_taxi = None

    while True:
        choice = input(MENU).strip().lower()
        if choice == "q":
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            bill_to_date += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == "__main__":
    main()
