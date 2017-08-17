
out_file = open("name.txt", "w")
user_name = input("What is your name? ")
print(user_name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
user_name = in_file.read().strip()
print("Your name is", user_name)
in_file.close()

in_file = open("numbers.txt", "r")
num_one = int(in_file.readline())
num_two = int(in_file.readline())
print(num_one + num_two)
in_file.close()

