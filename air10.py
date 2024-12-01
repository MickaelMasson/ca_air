    # Note à moi-même;
    # objet_fichier = open(chemin, "r")
    # objet_fichier.close()
    # le probleme de cette méthose, c'est qu'il important de .close() 
    # car ça peut créer des problèmes si plus tard on cherche à 
    # ouvrir de nouveau le fichier déjà ouvert
    # l'autre méthode qui évite le close() car il ferme le fichier 
    # dès qu'il sort du bloc d'instruction with:

"""Afficher le contenu"""
import sys
import os

# Fonctions utilisées
def read_file(file_name: str, path: str) -> str:
    file_name_with_path = path + file_name
    with open(file_name_with_path, "r") as objet_file :
        file_content = objet_file.read()
        return file_content

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list, number_of_argument: int) -> bool:
    if len(arguments) != number_of_argument :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True
    
def is_valid_file_name(argument: str, file_type_expected: str) -> bool:
    if not argument.endswith(file_type_expected) :
            print("Error, vous devez saisir le nom du fichier complet : fichier.txt")
            return False
    return True

def is_exist_file(file_name: str, path: str) -> bool:
    file_name_with_path = path + file_name
    if not os.path.exists(file_name_with_path) :
        print("Error, Le fichier demandé n'a pas été trouvé, vérifiez le chemin et l'orthographe")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list[str] :
    arguments = sys.argv[1:]
    return arguments

def get_path() -> str:
    full_path = sys.argv[0]
    index_last_slash = full_path.rfind("/")
    path = full_path[0:index_last_slash + 1]
    return path

# Partie 3 : Résolution
def display_file_content() :
    arguments = get_arguments()
    number_of_argument_expected = 1
    if not is_valid_arguments(arguments, number_of_argument_expected) :
        return
    argument = arguments[0]
    file_type_expected = ".txt"
    if not is_valid_file_name(argument, file_type_expected) :
        return
    file_name = argument
    path = get_path()
    if not is_exist_file(file_name, path) :
        return
    print(read_file(file_name, path))

# Partie 4 : Affichage
display_file_content()
"""
Créez un programme qui affiche le contenu d’un fichier donné en argument.

Exemples d’utilisation :
$> cat a.txt
Je danse le mia
$> ruby exo.rb “a.txt”
Je danse le mia

Afficher error et quitter le programme en cas de problèmes d’arguments ou de fichier inaccessible.
"""