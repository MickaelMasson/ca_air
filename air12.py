"""Le roi des tris"""
import sys

# Fonctions utilisées
def partition(numbers, start, end) :
    pivot = numbers[end]
    j = start
    for i in range(start,end) :
        if numbers[i] <= pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1
    numbers[j], numbers[end] = numbers[end], numbers[j]
    return j

def get_quicksort(numbers: list[int], start=0, end=None) -> list[int]:
    if end == None :
        end = len(numbers) - 1

    if end > start :
        pivot = partition(numbers, start, end)
        get_quicksort(numbers, start, pivot - 1)
        get_quicksort(numbers, pivot + 1, end)
    return numbers

# Partie 1 : Gestion d'erreur
def is_valid_arguments(arguments: list[str], number_of_argument: int) -> bool:
    if len(arguments) < number_of_argument :
        print("Error, le nombre d'arguments n'est pas valide")
        return False
    return True

def is_digit(string: str) -> bool:
    for character in string :
        if not "0" <= character <= "9" :
            print(f"Error, '{string}' n'est pas un nombre entier positif")
            return False
    return True

# Partie 2 : Parsing
def get_arguments() -> list[str] :
    arguments = sys.argv[1:]
    return arguments

# Partie 3 : Résolution
def display_sort_list() :
    arguments = get_arguments()
    min_number_of_argument_expected = 3
    if not is_valid_arguments(arguments, min_number_of_argument_expected) :
        return
    for argument in arguments :
        if not is_digit(argument) :
            return
    numbers = list(map(int, arguments))
    sort_numbers = get_quicksort(numbers)
    print(" ".join(map(str, sort_numbers)))

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