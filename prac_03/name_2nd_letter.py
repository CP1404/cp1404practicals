"""David Plummer"""


def main():
    name = get_name()
    print_name(name, 3)


def print_name(name, step=2):
    print(name[::step])


def get_name():
    name = input("Please enter your name: ")
    while name == "":
        print("Invalid input")
        name = input("Please enter your name: ")
    return name


main()
