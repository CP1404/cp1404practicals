"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    nun_of_months = int(input("How many months? "))

    for month in range(1, nun_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)


    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, nun_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:15.2f} Total: ${:15.2f}".format(month, income, total))


main()
