"""Meta exercice"""
import sys
import os
import subprocess

# Fonctions utilisées
class Counter_test_passed:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
    def get_value(self):
        return self.value
counter_test_passed = Counter_test_passed()

class Counter_test_passed_with_success:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
    def get_value(self):
        return self.value
counter_test_passed_with_success = Counter_test_passed_with_success()

class Counter_test_passed_with_failure:
    def __init__(self):
        self.value = 0
    def increment(self):
        self.value += 1
    def get_value(self):
        return self.value
counter_test_passed_with_failure = Counter_test_passed_with_failure()

def get_path() :
    full_path = sys.argv[0]
    index_last_slash = full_path.rfind("/")
    path = full_path[0:index_last_slash + 1]
    return path

def get_filename_with_path(file_name) :
    filename_with_path = get_path() + file_name
    return filename_with_path

def get_result_file(file_name, arguments_in) :
    filename_with_path = get_filename_with_path(file_name)

    if type(arguments_in) is list :
        result = subprocess.run(
        ["/bin/python3.13", filename_with_path] + arguments_in,  # Commande et argument
        capture_output=True,               # Capture la sortie
        text=True                          # Décoder en chaîne (pas en bytes)
)
    else :
        result = subprocess.run(
        ["/bin/python3.13", filename_with_path, arguments_in],  # Commande et argument
        capture_output=True,               # Capture la sortie
        text=True                          # Décoder en chaîne (pas en bytes)
)
    arguments_out = result.stdout
    return arguments_out

def is_success_test(file_name, arguments_in, good_answer) :
    arguments_out = get_result_file(file_name, arguments_in)
    if (arguments_out == good_answer or arguments_out.startswith(good_answer)) and good_answer != "" :
        counter_test_passed.increment()
        counter_test_passed_with_success.increment()
        return True
    else :
        counter_test_passed.increment()
        counter_test_passed_with_failure.increment()
        return False

def run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise) :
    if is_success_test(file_name, arguments_in, good_answer) :
        print(f"\033[32m{file_name} ({test_number}/{number_of_test_by_exercise}) : Success\033[0m")
    else : 
        print(f"\033[31m{file_name} ({test_number}/{number_of_test_by_exercise}) : Failure\033[0m")

# Partie 1 : Gestion d'erreur
def is_exist_file(file_name) :
    filename_with_path = get_filename_with_path(file_name)
    if not os.path.exists(filename_with_path) :
        print(f"\033[33mLe fichier {file_name} est introuvable, les tests pour ce fichier ne seront pas executé\033[0m")
        return False
    return True

# Partie 2 : Parsing

# Partie 3 : Résolution
def get_verif_exercise_air() :
    separator = "------------------------"
    
    file_name = "air00.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = ["jh", "kjh"]
        good_answer = "Error"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)
        #if is_success_test(file_name, arguments_in, good_answer) :
        #    display_success_message(file_name, test_number, number_of_test_by_exercise)
        #else : 
        #    display_failure_message(file_name, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = ["bonjour les gars"]
        good_answer = "bonjour\nles\ngars\n"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = ["bonjour\tles\tgars"]
        good_answer = "bonjour\nles\ngars"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = ["bonjour\nles\ngars"]
        good_answer = "bonjour\nles\ngars\n"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)

    file_name = "air01.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = ["Crevette"]
        good_answer = "Error, vous devez saisir 2 arguments"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = ["Crevette magique dans la mer des étoiles", "banane"]
        good_answer = "Error, Le dernier argument doit etre un séparateur present dans le premier argument"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = ["Crevette magique dans la mer des étoiles", "la"]
        good_answer = "Crevette magique dans \n mer des étoiles"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = ["Hakuna Matata. Mais quelle phrase magnifique !", "quelle"]
        good_answer = "Hakuna Matata. Mais \n phrase magnifique !"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)

    file_name = "air02.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = ["un seul argument"]
        good_answer = "Error"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = ["je", "test", "des", "trucs", " "]
        good_answer = "je test des trucs"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = ["Hakuna", "Matata", "Quel", "chant", "fantastique", "!", "&"]
        good_answer = "Hakuna&Matata&Quel&chant&fantastique&!"
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)

    file_name = "air03.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)

    file_name = "air04.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)
    
    file_name = "air05.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)

    file_name = "air06.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)
    
    file_name = "air07.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)
    
    file_name = "air08.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)

    file_name = "air09.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)
    
    file_name = "air10.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)

    file_name = "air11.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)
    
    file_name = "air12.py"
    number_of_test_by_exercise = 4
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

        #test
        test_number += 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)

    file_name = "air15.py"
    number_of_test_by_exercise = 1
    if is_exist_file(file_name) :
        #test
        test_number = 1
        arguments_in = [""]
        good_answer = ""
        run_test(file_name, arguments_in, good_answer, test_number, number_of_test_by_exercise)

    print(separator)

    print(f"Total success : {counter_test_passed_with_success.get_value()} / {counter_test_passed.get_value()}")
    print(f"Total Failure : {counter_test_passed_with_failure.get_value()}")


# Partie 4 : Affichage
get_verif_exercise_air()
"""
Créez un programme qui vérifie si les exercices de votre épreuve de l’air sont présents dans le répertoire et qu’ils fonctionnent (sauf celui là). Créez au moins un test pour chaque exercice.


Exemples d’utilisation :
$> python exo.py
air00 (1/3) : success
air00 (2/3) : success
air00 (3/3) : success
air01 (1/2) : success
air01 (2/2) : failure
air02 (1/1) : success
... 
Total success: (56/62)

Bonus : trouvez le moyen d’utiliser du vert et du rouge pour rendre réussites et échecs plus visibles.
"""