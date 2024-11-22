"""
"""
import sys

# Fonctions utilisées

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 3 :
        print("Error, ")
        return False
    return True
    
def is_digit(arguments) :
    for argument in arguments :
        if not argument.lstrip("-").isdigit() :
            print("Error, ")
            return False
    return True

def is_valid_number(arguments) :
    number = int(arguments[0])
    if number < 1 :
        print(-1)
        return False
    return True

def is_alpha(arguments):
    for argument in arguments :
        if not argument.isalpha() :
            print("Vous devez saisir des arguments composés de lettres a-z / A-Z")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display() :
    

# Partie 4 : Affichage
display()
"""

"""