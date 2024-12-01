"""Un seul à la fois"""
import sys

# Fonctions utilisées
def get_string_without_double_character(argument: str) -> str :
    news_string = argument[0]
    for character in argument[1:] :
        last_letter = news_string[-1]
        if character != last_letter :
            news_string = news_string + character
    return news_string

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) != number_of_argument :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True
    
# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_string_without_double_character() :
    arguments = get_arguments()
    number_of_argument_expected = 1
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    argument = arguments[0]
    print(get_string_without_double_character(argument))

# Partie 4 : Affichage
display_string_without_double_character()
"""
Créez un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents.


Exemples d’utilisation :
$> python exo.py “Hello milady,   bien ou quoi ??”
Helo milady, bien ou quoi ?


Afficher error et quitter le programme en cas de problèmes d’arguments.

"""