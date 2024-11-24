"""Mélanger deux tableaux triés"""
import sys

# Fonctions utilisées
def sort_fusion_numbers(arguments) :
    arguments.remove("fusion")
    numbers = list(map(int, arguments))
    new_sort_numbers = sorted(numbers)
    new_sort_list = list(map(str, new_sort_numbers))
    return new_sort_list

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 3 :
        print("Error, vous devez saisir au moins 3 arguments")
        return False
    return True

def is_valid_separator(arguments) :
    if not "fusion" in arguments :
        print("Error, vous devez avoir un argument nommé 'fusion'")
        return False
    return True

def is_digit(arguments) :
    for argument in arguments :
        if not argument.lstrip("-").isdigit() and argument != "fusion":
            print("Error, hormis 'fusion' les arguments doivent être des entiers")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_sort_numbers() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_valid_separator(get_arguments()) :
        return
    if not is_digit(get_arguments()) :
        return
    print(" ".join(sort_fusion_numbers(get_arguments())))

# Partie 4 : Affichage
display_sort_numbers()
"""
Créez un programme qui fusionne deux listes d’entiers triées en les gardant triées, les deux listes seront séparées par un “fusion”.

Utilisez une fonction de ce genre (selon votre langage) :
sorted_fusion(array1, array2) {
	# your algo
	return (new_array)
}


Exemples d’utilisation :
$> ruby exo.rb 10 20 30 fusion 15 25 35
10 15 20 25 30 35


Afficher error et quitter le programme en cas de problèmes d’arguments.
"""