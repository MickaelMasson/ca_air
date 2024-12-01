"""Split"""
import sys

# Fonctions utilisées
def get_split_argument(argument: str, separator: str) -> list:
    for character in separator :
        argument = argument.replace(character, "|")
    news_arguments = argument.split("|")
    return news_arguments

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, index_number: int) -> bool :
    if len(arguments) != index_number :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_split_arguments() :
    arguments = get_arguments()
    number_of_argument_expected = 1
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    argument = arguments[0]
    separator = "\n\t "
    print("\n".join(get_split_argument(argument, separator)))    

# Partie 4 : Affichage
display_split_arguments()
"""
Créez un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations, retours à la ligne).

Votre programme devra utiliser une fonction prototypée comme ceci :
ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
	# votre algorithme
	return (tableau)
}


Exemples d’utilisation :
$> python exo.py “Bonjour les gars”
Bonjour
les
gars

Afficher error et quitter le programme en cas de problèmes d’arguments.
"""