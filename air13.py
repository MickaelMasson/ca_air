"""Meta exercice"""
import sys
import os
import json
import subprocess

separator = "-----------------------------------------------------------------------------------------------------"

# Fonctions utilisées

def get_paths() -> tuple[str, str]:
    full_path = sys.argv[0]
    index_last_slash = full_path.rfind("/")
    path = full_path[:index_last_slash + 1]

    index_next_last_slash = path[:-1].rfind("/")
    parent_path = path[:index_next_last_slash + 1]

    return path, parent_path

def get_result_file(script_path: str, arguments_in: list[str]) -> str:
    python_path = "/bin/python3.13"
    result = subprocess.run(
                    [python_path, script_path] + arguments_in,
                    capture_output=True,
                    text=True
                )
    argument_out = result.stdout[:-1]
    return argument_out

def display_counter_test_passed(test_passed_with_success: int, test_passed: int) :
    print(f"\n                                 ###################################")
    print(f"                                 #                                 #")
    print(f"                                 #   Total success : {test_passed_with_success} / {test_passed}     #")
    print(f"                                 #   Total Failure : {(test_passed - test_passed_with_success)}             #")
    print(f"                                 #                                 #")
    print(f"                                 ###################################\n")

# Partie 1 : Gestion d'erreur

def is_every_file_keys_completed(id_file: str, level: str, file_name: str) -> bool:
    if id_file == "" or level == "" or file_name == "":
        print(separator + f"\n\033[33m  Pour que l'entrée soit valide, vous devez complétez toutes ces clés dans le fichier json\033[0m\n    'id_file'   : {id_file}\n    'file_name' : {file_name}\n    'level'     : {level}\n" + separator)
        return False
    return True

def is_exists_file(script_path: str) -> bool:
    if not os.path.exists(script_path) :
        print(separator + f"\n\033[31m  Fichier non trouvé :\033[0m {script_path}\n\033[33m    les tests ne peuvent pas etre executé\033[0m\n" + separator)
        return False
    return True

def is_id_test_key_completed(id_test: str, id_file: str, level: str, file_name: str) :
    if id_test == "" :
        print(separator + f"\n\033[33m  Vous devez complétez la clé 'id_test' dans le fichier json\033[0m\n    'id_file'   : {id_file}\n    'file_name' : {file_name}\n    'level'     : {level}\n    'tests'\n       └── 'id_test' :\n\033[33m    le test n'est pas executé\033[0m\n" + separator)
        return False
    return True 
                
# Partie 2 : Parsing

# Partie 3 : Résolution
def display_result_test():
    path, parent_path = get_paths()
    json_name = "check_exercises.json"

    with open(path + json_name, "r") as file:
        data_json = json.load(file)

    test_passed_with_success = 0
    test_passed = 0

    for file_entry in data_json["files"]:
        id_file = file_entry["id_file"]
        file_name = file_entry["file_name"]
        level = file_entry["level"]
        tests = file_entry["tests"]

        exercise_path = parent_path + f"ca_{level}/{file_name}"

        if not is_every_file_keys_completed(id_file, level, file_name) :
            continue        
        if not is_exists_file(exercise_path) :
            continue

        for test in tests:
            number_test = tests.index(test) + 1
            total_of_test_by_file = len(tests)

            id_test = test["id_test"]
            arguments = test["arguments"]
            expected_answer = test["answer"]

            if not is_id_test_key_completed(id_test, id_file, level, file_name) :
                continue

            answer = get_result_file(exercise_path, arguments)

            if answer == expected_answer:
                test_passed_with_success += 1
                test_passed += 1
                print(f"\033[32m  {file_name} ( {number_test} / {total_of_test_by_file} ) : Success\033[0m")
            else:
                test_passed += 1
                print(separator)
                print(f"\033[31m  {file_name} ( {number_test} / {total_of_test_by_file} ) : Failure\033[0m")
                print(f"    Les arguments saisis :   --> {arguments} <--")
                print(f"    La réponse attendue :    --> {expected_answer} <--")
                print(f"    La réponse reçue :       --> {answer} <--")
                print(separator)

    display_counter_test_passed(test_passed_with_success, test_passed)

# Partie 4 : Affichage
display_result_test()

"""Créez un programme qui vérifie si les exercices de votre épreuve de l’air 
sont présents dans le répertoire et qu’ils fonctionnent (sauf celui là). 
Créez au moins un test pour chaque exercice.


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