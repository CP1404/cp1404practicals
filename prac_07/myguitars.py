"""
CP1404/CP5632 Practical 07 - Program for managing a list of guitars.
Reads guitar data from file, displays sorted list, and allows adding new guitars.
Estimate: 15 min
Actual: 15 min
"""
from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    print("These are my guitars:")
    for guitar in guitars:
        vintage_str = " (Vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage_str}")

    print("\nAdd new guitars (leave name blank to finish):")
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ").strip()

    guitars.sort()
    save_guitars(FILENAME, guitars)
    print(f"\n{len(guitars)} guitars saved to {FILENAME}.")

def load_guitars(filename):
    guitars = []
    try:
        with open(filename, 'r') as infile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(',')
                name = parts[0]
                year = int(parts[1])
                cost = float(parts[2])
                guitar = Guitar(name, year, cost)
                guitars.append(guitar)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return guitars

def save_guitars(filename, guitars):
    with open(filename, 'w') as outfile:
        for guitar in guitars:
            cost = guitar.cost
            cost_str = str(int(cost)) if cost.is_integer() else str(cost)
            outfile.write(f"{guitar.name},{guitar.year},{cost_str}\n")

if __name__ == "__main__":
    main()
