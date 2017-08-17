
x = int(input("Enter the first number: "))
y = int(input("Enter the last number: "))
for i in range(int(x), int(y + 1), 1):
    if i % 2 == 0:
        print(i, end=" ")
print()
for i in range(int(x), int(y + 1), 1):
    if i % 2 == 1:
        print(i,  end=" ")
print()
for i in range(int(x), int(y + 1), 1):
    if i**i % 2 == 0:
        print(i**i,  end=" ")
print()
#
# introduzca el primer numero
# introduzca el ultimo numero
# numeros pares
# numeros impares
# numero al cuadrado
