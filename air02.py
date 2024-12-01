"""Concat"""
import sys

# Fonctions utilisées
def get_new_string(arguments: list[str], separator: str) -> str:
    news_string = separator.join(arguments)
    return news_string

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, index_number: int) -> bool :
    if not len(arguments) > index_number :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_news_string() :
    arguments = get_arguments()
    min_number_of_argument_expected = 2
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    main_arguments = arguments[:-1]
    separator = arguments[-1]
    print(get_new_string(main_arguments, separator))

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