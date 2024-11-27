"""Le roi des tris"""
import sys

# Fonctions utilisées
def partition(list, start, end) :
    pivot = list[end]
    j = start
    for i in range(start,end) :
        if list[i] <= pivot:
            list[i], list[j] = list[j], list[i]
            j += 1
    list[j], list[end] = list[end], list[j]
    return j

def sort_quicksort(list, start=0, end=None) :
    if end == None :
        end = len(list) - 1

    if end > start :
        pivot = partition(list, start, end)
        sort_quicksort(list, start, pivot - 1)
        sort_quicksort(list, pivot + 1, end)
    return list

# Partie 1 : Gestion d'erreur
def is_valid_number_of_arguments(arguments) :
    if len(arguments) < 3 :
        print("Error, vous devez saisir au moins 2 arguments")
        return False
    return True
    
def is_digit(arguments) :
    for argument in arguments :
        if not argument.lstrip("-").isdigit() :
            print("Error, tous vos arguments doivent être des nombres entiers")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_sort_list() :
    if not is_valid_number_of_arguments(get_arguments()) :
        return
    if not is_digit(get_arguments()) :
        return
    print(" ".join(sort_quicksort(get_arguments())))

# Partie 4 : Affichage
display_sort_list()
"""
Créez un programme qui trie une liste de nombres. Votre programme devra implémenter 
l’algorithme du tri rapide (QuickSort).

Vous utiliserez une fonction de cette forme (selon votre langage) :
my_quick_sort(array) {
	# votre algorithme
	return (new_array)
}

Exemples d’utilisation :
$> python exo.py 6 5 4 3 2 1
1 2 3 4 5 6

Afficher error et quitter le programme en cas de problèmes d’arguments.

Wikipedia vous présentera une belle description de cet algorithme de tri.

"""