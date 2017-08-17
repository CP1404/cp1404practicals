


def english_dialect():

    total_price = 0
    number_of_items = int(input("Enter number of items: "))
    while number_of_items < 0:
        print("Invalid number of items")
        number_of_items = int(input("Enter number of items: "))
    for i in range(number_of_items):
        price_per_item = float(input("Price of item: "))
        total_price += price_per_item

    if total_price > 100:
        total_price *= 0.9

    print("The total price for ", number_of_items, " items is $", total_price, " with the discount added")


def spanish_dialect():
    total_price = 0
    number_of_items = int(input("introduzca el nombre de los articulos: "))
    while number_of_items < 0:
        print("articulo invalido")
        number_of_items = int(input("precio por articulo: "))
    for i in range(number_of_items):
        price_per_item = float(input("precio por articulo: "))
        total_price += price_per_item

    if total_price > 100:
        total_price *= 0.9

    print("precio total por ", number_of_items, " articulos $", total_price, " incluido el descuento")

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
# introduzca el nombre de los articulos
# articulo invalido
# precio por articulo
# precio total por 5, articulos 100,incluido el descuento
