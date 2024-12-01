"""Sur chacun d’entre eux"""
import sys

# Fonctions utilisées
def add_to_numbers(numbers: list[int], operator_number: int) -> list[int]:
    result_numbers = []
    for number in numbers :
        result_numbers.append(number + operator_number)
    return result_numbers

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) < number_of_argument :
        print("Error, vos arguments ne sont pas valide")
        return False
    return True

def is_digit(string: str) -> bool :
    string = string.lstrip("-+")
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier")
            return False
    return True

def is_valid_operator(operator: str) -> bool :
    if operator[0] != "+" and operator[0] != "-" :
            print("Error, vous devez saisir un operateur au dernier argument")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_add_to_numbers() :
    arguments = get_arguments()
    min_number_of_argument_expected = 2
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    for argument in arguments :
        if not is_digit(argument) :
            return
    operator = arguments[-1]
    if not is_valid_operator(operator) :
        return
    base_numbers = list(map(int, arguments[0:-1]))
    operator_number = int(arguments[-1])
    new_numbers = add_to_numbers(base_numbers, operator_number)
    new_str_list = list(map(str, new_numbers))
    print(" ".join(new_str_list))

# Partie 4 : Affichage
display_add_to_numbers()
"""
Créez un programme qui est capable de reconnaître et de faire une opération (addition ou soustraction) sur chaque entier d’une liste.

Exemples d’utilisation :
$> ruby exo.rb 1 2 3 4 5 “+2”
3 4 5 6 7

$> ruby exo.rb 10 11 12 20 “-5”
5 6 7 15


L’opération à appliquer sera toujours le dernier élément.

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""