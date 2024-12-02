"""Meta exercice"""
import sys
import os
import json
import subprocess

separator = "----------------------------------------------------------------------------------------------------"

# Fonctions utilisées

def get_path() :
    full_path = sys.argv[0]
    index_last_slash = full_path.rfind("/")
    path = full_path[:index_last_slash + 1]

    index_next_last_slash = path[:-1].rfind("/")
    parent_path = path[:index_next_last_slash + 1]

    return path, parent_path

def get_result_file(script_path: str, arguments_in) -> str:
    if type(arguments_in) is list :
        result = subprocess.run(
        ["/bin/python3.13", script_path] + arguments_in,
        capture_output=True,
        text=True
)
    elif arguments_in == "" :
        result = subprocess.run(
        ["/bin/python3.13", script_path],
        capture_output=True,
        text=True
)
    else :
        result = subprocess.run(
        ["/bin/python3.13", script_path, arguments_in],
        capture_output=True,
        text=True
)
    argument_out_with_n = result.stdout
    list_arguments_out = []
    argument_out = argument_out_with_n[:-1]
    list_arguments_out.append(argument_out)
    return argument_out

# Partie 1 : Gestion d'erreur

def is_every_keys_completed(id_file, level, file_name) -> bool:
    if id_file == level == file_name == "" :
        return False
    elif id_file == "" or level == "" or file_name == "":
        print(separator + f"\n\033[33m L'un des objets 'files' n'est pas valide, vous devez complétez toutes ces clés dans le fichier json\033[0m\n    'id_file'   : {id_file}\n    'file_name' : {file_name}\n    'level'     : {level}\n" + separator)
        return False
    return True

def is_exist_file(script_path):
    if not os.path.exists(script_path) :
        print(separator + f"\n\033[31mFichier non trouvé :\033[0m {script_path}\n\033[33m    les tests ne peuvent pas etre executé\033[0m\n" + separator)
        return False
    return True

# Partie 2 : Parsing

# Partie 3 : Résolution
def display_result_test():
    path, parent_path = get_path()
    json_name = "check_exercises.json"
    json_full_path = path + json_name
    test_passed_with_success = 0
    test_passed = 0

    with open(json_full_path, "r") as file:
        data_json = json.load(file)
 
    for file_entry in data_json["files"]:
        id_file = file_entry["id_file"]
        file_name = file_entry["file_name"]
        level = file_entry["level"]
        tests = file_entry["test"]
        exercise_path = parent_path + f"ca_{level}/{file_name}"

        if not is_every_keys_completed(id_file, level, file_name) :
            continue        
        if not is_exist_file(exercise_path) :
            continue
        
        number_of_test_by_file = 0
        for test in tests :
            if test["id_test"] != "" :
                number_of_test_by_file += 1

        for test in tests:
            id_test = test["id_test"]
            arguments = test["arguments"]
            expected_answer = test["answer"]
            if id_test == "" :
                continue

            answer = get_result_file(exercise_path, arguments)
            
            if answer == expected_answer:
                print(f"\033[32m{file_name} ( {id_test} / {number_of_test_by_file} ) : Success\033[0m")
                test_passed_with_success += 1
                test_passed += 1
            else:
                print(separator)
                print(f"\033[31m{file_name} ( {id_test} / {number_of_test_by_file} ) : Failure\033[0m")
                print(f"    Les arguments saisis :   --> {arguments} <--")
                print(f"    La réponse attendue :    --> {expected_answer} <--")
                print(f"    La réponse reçue :       --> {answer} <--")
                print(separator)

                test_passed += 1
                

        
    print(f"\n    ###################################")
    print(f"    #                                 #")
    print(f"    #   Total success : {test_passed_with_success} / {test_passed}     #")
    print(f"    #   Total Failure : {(test_passed - test_passed_with_success)}             #")
    print(f"    #                                 #")
    print(f"    ###################################\n")

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








"""import os
import json
import importlib.util

# Chemin vers le fichier JSON
json_path = "check_exercises.json"

# Charger le JSON
with open(json_path, "r") as file:
    data = json.load(file)

# Parcourir les fichiers dans le JSON
for file_entry in data["files"]:
    file_name = file_entry["file_name"]
    level = file_entry["level"]
    tests = file_entry["test"]

    # Construire le chemin du fichier Python
    script_path = os.path.join(os.path.dirname(json_path), f"../ca_{level}/{file_name}")

    # Vérifier si le fichier existe
    if not os.path.exists(script_path):
        print(f"Fichier non trouvé : {script_path}")
        continue

    # Charger dynamiquement le module Python
    spec = importlib.util.spec_from_file_location(file_name, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Exécuter les tests
    for test in tests:
        id_test = test["id_test"]
        arguments = test["arguments"]
        expected_answer = test["answer"]

        # Préparer les arguments pour la fonction principale du fichier
        args = arguments.split() if arguments else []

        # Appeler la fonction principale et comparer la réponse
        if hasattr(module, "main"):
            try:
                # Appeler la fonction principale
                result = module.main(*args)
                if str(result) == expected_answer:
                    print(f"Test {id_test} dans {file_name} : Réussi")
                else:
                    print(f"Test {id_test} dans {file_name} : Échoué (Attendu: {expected_answer}, Obtenu: {result})")
            except Exception as e:
                print(f"Erreur lors de l'exécution du test {id_test} dans {file_name} : {e}")
        else:
            print(f"Le fichier {file_name} ne contient pas de fonction main()")"""