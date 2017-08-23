
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])
numbers[0] = 10
numbers[6] = 1
print(numbers)
print(numbers, 2, 1, 1,)
print(9 in numbers)


numbers = []
for i in range(5):
 number = int(input("Number: "))
 numbers.append(number)
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))