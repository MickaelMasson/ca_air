"""Afficher une pyramide"""
import sys

# Fonctions utilisées
def get_pyramid(arguments) :
    character = arguments[0]
    number_of_floors = int(arguments[1])
    for i in range(number_of_floors) :
         print(" " * (number_of_floors - (i + 1)) + character * ((2 * i) + 1))
    return

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) != 2 :
        print("Error, vous devez saisir 2 arguments")
        return False
    return True

def is_single_character(arguments):
    argument = arguments[0]
    if len(argument) != 1 :
            print("Vous devez saisir un seul caractère en 1er arguments")
            return False
    return True
    
def is_digit_number_of_floors(arguments) :
    argument = arguments[1]
    if not argument.isdigit() :
            print("Error, vous devez entrez un entier positif en 2eme argument")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_pyramid() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_digit_number_of_floors(get_arguments()) :
        return
    if not is_single_character(get_arguments()) :
        return
    get_pyramid(get_arguments())

# Partie 4 : Affichage
display_pyramid()
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