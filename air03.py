"""Chercher l’intrus"""
import sys

# Fonctions utilisées
def get_single_arguments(arguments) :
    single_arguments = []
    for argument in arguments :
        if argument in single_arguments :
            single_arguments.remove(argument)
        else :
            single_arguments.append(argument)
    return single_arguments

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 1 :
        print("Error, ")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_single_argument() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    print(", ".join(get_single_arguments(get_arguments())))

# Partie 4 : Affichage
display_single_argument()
"""
Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.

Exemples d’utilisation :
$> python exo.py 1 2 3 4 5 4 3 2 1
5

$> python exo.py bonjour monsieur bonjour
monsieur

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""