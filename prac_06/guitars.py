"""CP1404/CP5632 Practical 06 – Use the Guitar class.

Estimate: 20 min
Actual: 20min
"""

from prac_06.guitar import Guitar, CURRENT_YEAR


def main() -> None:
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name:
        year = _read_int("Year: ")
        cost = _read_float("Cost: $")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    if not guitars:
        print("No guitars :(  Bye!")
        return

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_tag = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
              f"worth ${guitar.cost:10,.2f}{vintage_tag}")


def _read_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Input must be a non-negative integer")


def _read_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Input must be a non-negative number")


if __name__ == "__main__":
    main()
