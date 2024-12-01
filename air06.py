"""Contrôle de pass sanitaire"""
import sys

# Fonctions utilisées
def remove_arguments_with_substring(arguments: list[str], substring: str) -> list[str] :
    arguments_without_substring = []
    for argument in arguments :
        for i in range(len(argument) - len(substring) + 1) :
            is_found = False
            if argument[i:i + len(substring)] == substring :
                is_found = not is_found
                break
        if not is_found :
            arguments_without_substring.append(argument)               
    return arguments_without_substring

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool :
    if len(arguments) < number_of_argument :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_arguments_without_substring() :
    arguments = get_arguments()
    min_number_of_argument_expected = 2
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return

    base_arguments = list(map(str.lower, arguments[0:-1]))
    substring = str(arguments[-1]).lower()

    arguments_without_substring = remove_arguments_with_substring(base_arguments, substring)
    title_arguments = list(map(str.title, arguments_without_substring))
    print(" ".join(title_arguments))

# Partie 4 : Affichage
display_arguments_without_substring()
"""
Créez un programme qui supprime d’un tableau tous les éléments qui ne contiennent 
pas une autre chaîne de caractères.

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