"""Chercher l’intrus"""
import sys

# Fonctions utilisées
def get_singles_arguments(arguments: list[str]) -> list[str] :
    singles_arguments = []
    for argument in arguments :
        is_pair = False
        for single_argument in singles_arguments :
            if single_argument == argument :
                is_pair = True
                break
        if is_pair :
            singles_arguments.remove(argument)
        else :
            singles_arguments.append(argument)

    return singles_arguments

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) < number_of_argument :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_single_arguments() :
    arguments = get_arguments()
    min_number_of_argument_expected = 2
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    print(", ".join(get_singles_arguments(arguments)))

# Partie 4 : Affichage
display_single_arguments()
"""
Créez un programme qui retourne la valeur d’une liste qui n’a pas de paire.

Exemples d’utilisation :
$> python exo.py 1 2 3 4 5 4 3 2 1
5

$> python exo.py bonjour monsieur bonjour
monsieur

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""