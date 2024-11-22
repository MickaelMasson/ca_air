"""Concat"""
import sys

# Fonctions utilisées
def get_new_string(arguments) :
    separator = arguments[-1]
    arguments = arguments[0:-1]
    news_string = separator.join(arguments)
    return news_string

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 2 :
        print("Error, vous devez saisir 2 arguments")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_news_string() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    print(get_new_string(get_arguments()))

# Partie 4 : Affichage
display_news_string()
"""
Créez un programme qui transforme un tableau de chaînes de caractères 
en une seule chaîne de caractères. Espacés d’un séparateur donné en dernier argument au programme.

Utilisez une fonction de ce genre (selon votre langage) :
ma_fonction(array_de_strings, separateur) {
	# votre algorithme
	return (string)
}


Exemples d’utilisation :
$> python exo.py “je” “teste” “des” “trucs” “ “
Je teste des trucs


Afficher error et quitter le programme en cas de problèmes d’arguments.

"""