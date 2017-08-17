# """
# CP1404/CP5632 - Practical
# Broken program to determine score status
# """
#
# # TODO: Fix this!
#12332432432432
# score = float(input("Enter score: "))
# if score < 0:lff
#     print("Invalid score")
# else:
#     if score > 100:
#         print("Invalid score")
#     if score > 50:
#         print("Passable")
#     if score > 90:
#     print("Excellent")
# if score < 50:
#     print("Bad")

# ponga el puntage
# puntage incorrecto
# excelente
# acceptable
# mal
#
# Escoja su idioma ingles o espanol
#


def main():

    language = int(input("choose your language/Escoja su idioma ingles o espanol: \n 1 for English \n 2 for Spanish "))
    if language == 1:
        english_dialect()
    elif language == 2:
        spanish_dialect()
    else:
        print(" 1 or 2 genius, start again")


def spanish_dialect():
    score = float(input("ponga el puntage: "))
    if score < 0 or score > 100:
        print("puntage incorrecto")
    elif score >= 90:
        print(" excelentet")
    elif score >= 50:
        print("acceptable")
    else:
        print("Mal")


def english_dialect():
    score = float(input(" "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")



main()