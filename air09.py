"""Rotation vers la gauche"""
import sys

# Fonctions utilisées
def shifts_to_the_left(arguments: list) -> list:
    first_argument = arguments[0]
    arguments.remove(first_argument)
    new_sort_arguments = arguments
    new_sort_arguments.append(first_argument)
    return new_sort_arguments

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) < number_of_argument :
        print("Error, le nombrre d'arguments n'est pas valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_new_sort_arguments() :
    arguments = get_arguments()
    min_number_of_argument_expected = 2
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    print(", ".join(shifts_to_the_left(arguments)))

# Partie 4 : Affichage
display_new_sort_arguments()
"""
Créez un programme qui décale tous les éléments d’un tableau vers la gauche. Le premier élément devient le dernier à chaque rotation.

Utilisez une fonction de ce genre (selon votre langage) :
ma_rotation(array) {
	# votre algorithme
	return (new_array)
}


Exemples d’utilisation :
$> python exo.py “Michel” “Albert” “Thérèse” “Benoit”
Albert, Thérèse, Benoit, Michel


Afficher error et quitter le programme en cas de problèmes d’arguments.

"""