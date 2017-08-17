"""  Program to calculate and display a user's bonus based on sales.
 If sales are under $1,000, the user gets a 10% bonus. If sales are
  $1,000 or over, the bonus is 15%. """


def english_dialect():
    sales = float(input("enter sales: $"))
    if sales < 1000:
        sales_bonus = sales * 1.1
    else:
        sales_bonus = sales * 1.15
    bonus = sales_bonus - sales
    print("Sales bonus is $", bonus)

def spanish_dialect():
    sales = float(input("total de ventas: $"))
    if sales < 1000:
        sales_bonus = sales * 1.1
    else:
        sales_bonus = sales * 1.15
    bonus = sales_bonus - sales
    print("ventas mas bonos $", bonus)

def main():

    language = int(input("choose your language/Escoja su idioma ingles o espanol: \n 1 for English \n 2 for Spanish "))
    if language == 1:
        english_dialect()
    elif language == 2:
        spanish_dialect()
    else:
        print(" 1 or 2 genius, start again")

main()

#
# #git hub
# sales = float(input("Enter sales: $"))
# if sales < 1000:
#     bonus = sales * 0.1
# else:
#     bonus = sales * 0.15
# print("Bonus is $", bonus, sep='')
#
# total de ventas
# ventas mas bonos