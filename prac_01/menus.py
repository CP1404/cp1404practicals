
def english_dialect():
get_name = input("Enter your name: ")
menu_choice = str.upper(input("(H)ello \n(G)oodbye \n(Q)uit"))

while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello ", get_name)
    elif menu_choice == "G":
        print("Goodbye", get_name)
    else:
        print("Invalid choice")
    menu_choice = str.upper(input("(H)ello \n(G)oodbye \n(Q)uit"))
print("Finished")
def main():

    language = int(input("choose your language/Escoja su idioma ingles o espanol: \n 1 for English \n 2 for Spanish "))
    if language == 1:
        english_dialect()
    elif language == 2:
        spanish_dialect()
    else:
        print(" 1 or 2 genius, start again")

main()
introduzca su nombre
hola
adios
seleccion invalida
final
suspender