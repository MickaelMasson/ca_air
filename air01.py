"""Split en fonction"""
import sys
import re

# Fonctions utilisées
def split_arguments(arguments) :
    separator = arguments[1]
    arguments = str(arguments[0])
    news_arguments = arguments.split(separator)
    return news_arguments

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) != 2 :
        print("Error, vous devez saisir 2 arguments")
        return False
    return True

def is_valid_separator(arguments):
    first_argument = arguments[0]
    second_argument = arguments[1]
    if not second_argument in first_argument :
        print("Le dernier argument doit etre un séparateur present dans le premier argument")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_news_arguments() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_valid_separator(get_arguments()) :
        return
    print("\n".join(split_arguments(get_arguments())))    

# Partie 4 : Affichage
display_news_arguments()
"""
Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.

Votre programme devra intégrer une fonction prototypée comme ceci :
ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
	# votre algorithme
	return (tableau)
}


Exemples d’utilisation :
$> python exo.py “Crevette magique dans la mer des étoiles” “la”
Crevette magique dans 
 mer des étoiles

Afficher error et quitter le programme en cas de problèmes d’arguments.

"""