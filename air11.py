"""Afficher une pyramide"""
import sys

# Fonctions utilisées
def display_pyramid(patern: str, number_of_floors: int) :
    for i in range(number_of_floors) :
         print(" " * (number_of_floors - (i + 1)) + patern * ((2 * i) + 1))
    return

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list[str], number_of_argument: int) -> bool:
    if len(arguments) != number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

def is_single_character(argument: str) -> bool:
    if len(argument) != 1 :
            print("Vous devez saisir un seul caractère en 1er arguments")
            return False
    return True
    
def is_digit(string: str) -> bool:
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier positif")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list[str] :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def get_pyramid() :
    arguments = get_arguments()
    number_of_argument_expected = 2
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    first_argument = arguments[0]
    if not is_single_character(first_argument) :
        return
    patern = first_argument
    second_argument = arguments[1]
    if not is_digit(second_argument) :
        return
    number_of_floors = int(second_argument)
    display_pyramid(patern, number_of_floors)

# Partie 4 : Affichage
get_pyramid()
"""
Afficher un escalier constitué d’un caractère et d’un nombre d’étages donné en paramètre.

Exemples d’utilisation :
$> ruby exo.rb O 5
    O
   OOO
  OOOOO
 OOOOOOO
OOOOOOOOO

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""