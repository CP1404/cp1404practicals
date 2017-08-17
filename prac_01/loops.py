
for i in range(1, 21, 2):
    print(i, end=" ")
print()

for i in range(0, 101, 10):
    print(i, end=" ")
print()

for i in range(20, 0, -1):
    print(i, end=" ")
print()



sales = float(input("enter sales: $"))
while sales >= 0:
    if sales < 1000:
        sales_bonus = sales * 1.1
    else:
        sales_bonus = sales * 1.15
    bonus = sales_bonus - sales
    print("Sales bonus is $", bonus)
    sales = float(input("enter sales: $"))
print("negative")

negativo


# Version 2 with loop
# Note the boundary condition (0 is valid sales) and general structure
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print("Bonus is $", bonus, sep='')
    sales = float(input("Enter sales: $"))
