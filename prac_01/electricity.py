
def spanish_dialect():
    get_tariff = int(input("introduzca el tariff 11 o 31?: "))
    get_daily_kWh = float(input("introduzca uso diario en kwh: "))
    billing_days = float(input("introduzca el numero de dias en servicios por mes: "))
    if get_tariff == 11:
        estimated_bill = TARIFF_11 * get_daily_kWh * billing_days
    else:
        estimated_bill = TARIFF_31 * get_daily_kWh * billing_days
    print("el costo estimado del servicio es ", estimated_bill)

def english_dialect():
    get_tariff = int(input("enter your Tariff 11 or 31?: "))
    get_daily_kWh = float(input("Enter your daily use in Kwh: "))
    billing_days = float(input("Enter number of billing days: "))
    if get_tariff == 11:
        estimated_bill = TARIFF_11 * get_daily_kWh * billing_days
    else:
        estimated_bill = TARIFF_31 * get_daily_kWh * billing_days
    print("your estimated bill is ", estimated_bill)


TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
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
# introduzca el tariff 11 o 31
# introduzca uso diario en kwh
# introduzca el numero de dias en servicios por mes
#  el costo estimado del servicio es
