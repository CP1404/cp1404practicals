import random

numbers_pre_line = 6
minimum = 1
maximum = 45

def main():
    num_of_quick_picks = int(input("How many quick picks? "))
    while num_of_quick_picks < 0:
        print("Please input valid number!")
        num_of_quick_picks = int(input("How many quick picks? "))

    for i in range(num_of_quick_picks):
        quick_pick = []
        for j in range(numbers_pre_line):
            number = random.randint(minimum, maximum)
            while number in quick_pick:
                number = random.randint(minimum, maximum)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))

main()
