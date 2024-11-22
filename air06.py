"""Contrôle de pass sanitaire"""
import sys

# Fonctions utilisées
def is_in_string(arguments):
    base_arguments = arguments[0:-1]
    ref_argument = str(arguments[-1]).lower()
    news_names = []
    for i in base_arguments :
        if not ref_argument in str(i).lower() :
            news_names.append(i)
    return news_names

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 2 :
        print("Error, vous devez saisir au moins 2 arguments")
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
    print(", ".join(is_in_string(get_arguments())))

# Partie 4 : Affichage
display()
"""
Créez un programme qui supprime d’un tableau tous les éléments qui ne contiennent pas une autre chaîne de caractères.

Utilisez une fonction de ce genre (selon votre langage) :
ma_fonction(array_de_strings, string) {
	# votre algorithme
	return (nouvel_array_de_strings)
}


Exemples d’utilisation :
$> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “t”
Michel

$> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “a”
Michel, Thérèse, Benoit



Afficher error et quitter le programme en cas de problèmes d’arguments.

"""