"""Rotation vers la gauche"""
import sys

# Fonctions utilisées
def shifts_to_the_left(arguments) :
    first_argument = arguments[0]
    arguments.remove(first_argument)
    new_list = arguments
    new_list.append(first_argument)
    return new_list

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 2 :
        print("Error, vous deve saisir au moins deux arguments")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_new_list() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    print(", ".join(shifts_to_the_left(get_arguments())))

# Partie 4 : Affichage
display_new_list()
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