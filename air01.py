"""Split en fonction"""
import sys

# Fonctions utilisées
def get_split_arguments(argument: str, separator: str) -> list[str]:
    arguments = argument.split(separator)
    return arguments

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) != number_of_argument :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

def is_valid_separator(argument: str, separator: str) -> bool:
    for i in range(len(argument) - len(separator) + 1) :
        if argument[i:i + len(separator)] == separator :
            return True
    print("Error, Le dernier argument doit etre un séparateur present dans le premier argument")
    return False

# Partie 2 : Parsing
def get_arguments() -> list :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_split_arguments() :
    arguments = get_arguments()
    number_of_argument_expected = 2
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    main_argument = arguments[0]
    separator = arguments[1]
    if not is_valid_separator(main_argument, separator) :
        return
    print("\n".join(get_split_arguments(main_argument, separator)))

# Partie 4 : Affichage
display_split_arguments()
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