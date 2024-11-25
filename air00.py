"""Split"""
import sys
import re

# Fonctions utilisées
def split_argument(arguments) :
    argument = arguments[0]
    news_arguments = re.split(r"[ \n\t]+", argument)
    return news_arguments

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) != 1 :
        print("Error, vous devez saisir une chaine de caractère")
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
    print("\n".join(split_argument(get_arguments())))    

# Partie 4 : Affichage
display_news_arguments()
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