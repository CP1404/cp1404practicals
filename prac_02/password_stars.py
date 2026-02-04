def get_password():
    password = input("Enter your password: ")
    while len(password) < 8:
        print("Password too short")
        password = input("Enter your password: ")
    return password


def print_asterisks(password):
    print('*' * len(password))


def main():
    password = get_password()
    print_asterisks(password)


if __name__ == "__main__":
    main()
