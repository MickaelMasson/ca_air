"""Sur chacun d’entre eux"""
import sys

# Fonctions utilisées
def get_string_result(arguments) :
    arguments_without_last = arguments[0:-1]
    operator_number = int(arguments[-1])
    numbers = list(map(int, arguments_without_last))
    new_numbers = list(map(lambda nombre: nombre + operator_number, numbers))
    news_list = list(map(str, new_numbers))
    return news_list

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 2 :
        print("Error, vous devez sasir au moins 2 arguments")
        return False
    return True
    
def is_digit(arguments) :
    for argument in arguments :
        if not argument.lstrip("-+").isdigit() :
            print("Error, vous devez saisir des nombre entiers")
            return False
    return True

def is_valid_operator(arguments) :
    argument = arguments[-1]
    if argument[0] != "+" and argument[0] != "-" :
            print("Error, vous devez saisir un operateur au dernier argument")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_digit(get_arguments()) :
        return
    if not is_valid_operator(get_arguments()) :
        return
    print(", ".join(get_string_result(get_arguments())))

# Partie 4 : Affichage
display()
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