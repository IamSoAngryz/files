"""
JSON File (Fisier JSON)
JSON    - format usor de interschimbare a datelor 
        - un stadard derivat de JavaScript
        - JavaScript Object Notation (notatia JavaScript)

Modulul json permite lucrul cu tipul de fisiere JSON (build-in in Python)
JSON este contruit pe baza a doua structuri:
1. o colectie de perechi nume/valoare (obiect)
2. o lista de valori (un tablou/array)

Lucrul cu fisiere JSON presupune:
1. Citirea / Deserializarea / Decodificare
    - conversie a unui fisier JSON intr-un obiect din Python
    (dict / list)
    Metoda jsdon.load(file_handler
2. Scrierea / Serializarea / Codificare
    - conversia unui obiect din Python intr-un fisier JSON
    - obiectele Python sunt transformate intr-o serie de bytes (caractere
    UNICODE) pentru a fi salvate si transmise in retea
    Metoda json.dump(object, file_handler)
Serializarea se poate realiza si cu conversia in string:
string_variable = json.dumps(object)

Deserializarea se paote realiza si pe baza unui string:
    object = json.loads(string_JSON)

"""

import json
import os

with open(os.path.join('data\data.json'), 'r') as f:
    data = json.load(f)
    print(f'Tipul datelor: {type(data)}')
    print(f'Deserializare JSON: {data}')

with open('data/employees.json', 'r') as f:
    employees_data = json.load(f)
    print(type(employees_data))
    print(f'Datele din json deserializare: {employees_data}')

employees_data['employees'][1]['salary'] = 9000
with open('data/new_employees.json', 'w') as f:
    json.dump(employees_data, f, indent = 2)

# serializarea intr-un string object:
employees_string = json.dumps(employees_data, indent = 2)
print(employees_string)

languages = """
    {
        "Python: 3.8
        "JavaScript": "ES6"
        "PHP": 7.4

    }
    """
languages_dict = json.loads(languages)
print(f'Deserializarea stringului: {languages_dict}')