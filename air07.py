"""Insertion dans un tableau trié"""
import sys

# Fonctions utilisées
def get_base_arguments_and_new_argument(arguments) :
    base_arguments = arguments[:-1]
    new_number = int(arguments[-1])
    return base_arguments, new_number

def add_number_sort_list(base_arguments, new_number):
    numbers = list(map(int, base_arguments))
    numbers.append(new_number)
    sorted_numbers = sorted(numbers)
    sorted_str_list = list(map(str, sorted_numbers))
    return sorted_str_list

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 3 :
        print("Error, vous devez saisir au moins 3 arguments")
        return False
    return True
    
def is_digit(arguments) :
    for argument in arguments :
        if not argument.lstrip("-").isdigit() :
            print("Error, tous vos arguments doivent être des entier")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_sorted_numbers() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_digit(get_arguments()) :
        return
    base_arguments, new_number = get_base_arguments_and_new_argument(get_arguments())
    print(" ".join(add_number_sort_list(base_arguments, new_number)))

# Partie 4 : Affichage
display_sorted_numbers()
"""
Créez un programme qui ajoute à une liste d’entiers triée un nouvel entier tout en gardant la liste triée dans l’ordre croissant. Le dernier argument est l’élément à ajouter.

Utilisez une fonction de ce genre (selon votre langage) :
sorted_insert(array, new_element) {
	# your algo
	return (new_array)
}


Exemples d’utilisation :
$> ruby exo.rb 1 3 4 2
1 2 3 4

$> ruby exo.rb 10 20 30 40 50 60 70 90 33
10 20 30 33 40 50 60 70 90


Afficher error et quitter le programme en cas de problèmes d’arguments.

"""