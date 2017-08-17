# # """
# # CP1404/CP5632 - Practical
# # Broken program to determine score status
# # """
# #

# #
# # score = float(input("Enter score: "))
# # if score < 0:
# #     print("Invalid score")
# # else:
# #     if score > 100:
# #         print("Invalid score")
# #     if score > 50:
# #         print("Passable")
# #     if score > 90:
# #     print("Excellent")
# # if score < 50:
# #     print("Bad")
#
# # ponga el puntage
# # puntage incorrecto
# # excelente
# # acceptable
# # mal
# #
# # Escoja su idioma ingles o espanol
# #
#
#
# def main():
#
#     language = int(input("choose your language/Escoja su idioma ingles o espanol: \n 1 for English \n 2 for Spanish "))
#     if language == 1:
#         english_dialect()
#     elif language == 2:
#         spanish_dialect()
#     else:
#         print(" 1 or 2 genius, start again")
#
#
# def spanish_dialect():
#     score = float(input("ponga el puntage: "))
#     if score < 0 or score > 100:
#         print("puntage incorrecto")
#     elif score >= 90:
#         print(" excelentet")
#     elif score >= 50:
#         print("acceptable")
#     else:
#         print("Mal")
#
#
# def english_dialect():
#     score = float(input(" "))
#     if score < 0 or score > 100:
#         print("Invalid score")
#     elif score >= 90:
#         print("Excellent")
#     elif score >= 50:
#         print("Passable")
#     else:
#         print("Bad")
#
#
#
# main()

"""
CP1404/CP5632 - Practical - Suggested Solution
Fixed program to determine score status, with function
"""


# Note boundary conditions (50 should be a pass, not > 50)
# Note efficiency and nesting; use the fewest number of if/elif as possible

def main():
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()