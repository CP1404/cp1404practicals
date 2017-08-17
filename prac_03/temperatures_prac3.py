#
# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
# print(MENU)
# choice = input(">>> ").upper()
# while choice != "Q":
#     if choice == "C":
#         celsius = float(input("Celsius: "))
#         fahrenheit = celsius * 9.0 / 5 + 32
#         print("Result: {:.2f} F".format(fahrenheit))
#     elif choice == "F":
#
#         fahrenheit = float(input("Fahrenheit : "))
#         celsius = 5 / 9 * (fahrenheit - 32)
#         print("Result: {:.2f} C".format(celsius))
#     else:
#         print("Invalid option")
#     print(MENU)
#     choice = input(">>> ").upper()
# print("Thank you.")

"""
CP1404/CP5632 - Practical - Suggested Solution
Temperature conversions
"""

MENU = print("C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit")

def main():
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            celsius = float(input("Enter Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "f":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print("Result is : {:.2f} C".format(celsius))
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").lower()
    print("Finished")


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()
