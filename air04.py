"""Un seul à la fois"""
import sys

# Fonctions utilisées
def get_sting_without_double_lettre(arguments) :
    argument = arguments[0]
    news_string = f"{argument[0]}"
    for i in range(1, len(argument)) :
        letter = argument[i]
        last_letter = news_string[-1]
        if not letter == last_letter :
            news_string = news_string + letter
    return news_string
        
# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 1 :
        print("Error, vous devez entrer au moins 1 argument")
        return False
    return True
    
# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_new_string() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    print(get_sting_without_double_lettre(get_arguments()))

# Partie 4 : Affichage
display_new_string()
"""
Créez un programme qui affiche une chaîne de caractères en évitant les caractères identiques adjacents.


Exemples d’utilisation :
$> python exo.py “Hello milady,   bien ou quoi ??”
Helo milady, bien ou quoi ?


Afficher error et quitter le programme en cas de problèmes d’arguments.

"""