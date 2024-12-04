"""Mélanger deux tableaux triés"""
import sys

# Fonctions utilisées
def get_two_list(arguments: list[str], separator:str) -> tuple[list[str], list[str]]:
    for i in range(len(arguments)) :
        if separator == arguments[i] :
            index_separator = i
            break
    first_list = arguments[:index_separator]
    second_list = arguments[index_separator + 1:]
    return first_list, second_list

def add_sorted_numbers_in_sorted_numbers(first_numbers: list[int], second_numbers: list[int]) -> list[int]:
    new_sorted_numbers = first_numbers
    for new_number in second_numbers :
        for i in range(len(first_numbers)) :
            if new_number < first_numbers[i] :
                new_sorted_numbers.insert(i, new_number)
                break
        else:
            new_sorted_numbers.append(new_number)
    return new_sorted_numbers

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) < number_of_argument :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

def is_valid_separator(arguments: list[str], separator: str) -> bool:
    for argument in arguments :
            if argument == separator :
                return True
    print(f"Error, vous devez saisir '{separator}' en argument pour séparer vos deux listes")
    return False

def is_digit(string: str) -> bool:
    string = string.lstrip("-")
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier positif")
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
    separator = "fusion"
    if not is_valid_separator(arguments, separator) :
        return
    first_list, second_list = get_two_list(arguments, separator)
    for argument in first_list :
        if not is_digit(argument) :
            return
    first_numbers = list(map(int, first_list))
    for argument in second_list :
        if not is_digit(argument) :
            return
    second_numbers = list(map(int, second_list))
    new_sorted_numbers = add_sorted_numbers_in_sorted_numbers(first_numbers, second_numbers)
    new_sorted_string_list = list(map(str, new_sorted_numbers))
    print(" ".join(new_sorted_string_list))

# Partie 4 : Affichage
display_new_sorted_numbers()
"""
Créez un programme qui fusionne deux listes d’entiers triées en les gardant triées, 
les deux listes seront séparées par un “fusion”.

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