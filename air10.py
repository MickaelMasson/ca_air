"""Afficher le contenu"""
import sys
import os

# Fonctions utilisées
def get_path() :
    full_path = sys.argv[0]
    index_last_slash = full_path.rfind("/")
    path = full_path[0:index_last_slash + 1]
    return path

def get_filename_with_path() :
    file_name = get_arguments()[0]
    filename_with_path = get_path() + file_name
    return filename_with_path

def read_file(arguments) :
    # Note à moi-même;
    # objet_fichier = open(chemin, "r")
    # objet_fichier.close()
    # le probleme de cette méthose, c'est qu'il important de .close() 
    # car ça peut créer des problèmes si plus tard on cherche à 
    # ouvrir de nouveau le fichier déjà ouvert
    # l'autre méthode qui évite le close() car il ferme le fichier 
    # dès qu'il sort du bloc d'instruction with:
    
    with open(get_filename_with_path(), "r") as objet_file :
        file_content = objet_file.read()
        return file_content

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) != 1 :
        print("Error, vous devez saisir un seul nom de fichier")
        return False
    return True
    
def is_valid_argument(arguments) :
    argument = arguments[0]
    if not argument.endswith(".txt") :
            print("Error, vous devez saisir le nom du fichier complet comme mon fichier.txt")
            return False
    return True

def is_exist_file() :
    if not os.path.exists(get_filename_with_path()) :
        print("Error, Le fichier demandé n'a pas été trouvé, vérifiez le chemin et l'orthographe")
        return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_file() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_valid_argument(get_arguments()) :
        return
    if not is_exist_file() :
        return
    print(read_file(get_arguments()))

# Partie 4 : Affichage
display_file()
"""
Créez un programme qui affiche le contenu d’un fichier donné en argument.

Exemples d’utilisation :
$> cat a.txt
Je danse le mia
$> ruby exo.rb “a.txt”
Je danse le mia

Afficher error et quitter le programme en cas de problèmes d’arguments ou de fichier inaccessible.
"""