
numbers = []
for num in range(5):
    number = int(input("Input a number: "))
    numbers.append(number)

print("First number", numbers[0])
print("Last number", numbers[-1])
print("Smallest number", min(numbers))
print("Largest number", max(numbers))
print("Average", sum(numbers) / len(numbers))

