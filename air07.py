"""Insertion dans un tableau trié"""
import sys

# Fonctions utilisées
def add_number_in_sorted_numbers(numbers: list[int], new_number: int) -> list[int]:
    new_numbers = numbers
    for i in range(len(numbers)) :
        if new_number < numbers[i] :
            new_numbers.insert(i, new_number)
            return new_numbers
    new_numbers.append(new_number)
    return new_numbers

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) < number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

def is_digit(string: str) -> bool:
    string = string.lstrip("-")
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_new_sorted_numbers() :
    arguments = get_arguments()
    min_number_of_argument_expected = 3
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    for argument in arguments :
        if not is_digit(argument) :
            return
    numbers = list(map(int, arguments[:-1]))
    new_number = int(arguments[-1])
    new_sort_numbers = add_number_in_sorted_numbers(numbers, new_number)
    new_sorted_string_list = list(map(str, new_sort_numbers))
    print(" ".join(new_sorted_string_list))

# Partie 4 : Affichage
display_new_sorted_numbers()
"""
Créez un programme qui ajoute à une liste d’entiers triée un nouvel entier tout en 
gardant la liste triée dans l’ordre croissant. Le dernier argument est l’élément à ajouter.

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