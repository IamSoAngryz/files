"""
YAML File
YAML    = un format de interschimbare a datelor
        - Yet Another Markup Language
        - standard de serializare a datelor (asemanator JSON)
Link:   https://yaml.org/
Modulul yaml lucreaza cu fisiere yaml
Instalare:
    pip install pyyaml
pip = Package Installer pentry Python

Formatul YAML este structurat pe:
1. perechi cheie (nume): valoare (reprezentate fara {, } separate prin new line)
2. tablouri de valori   (reprezentate cu [, ])
YAML este folosit la:
    - schimb de informatii in retea
    - salvari de configuratii (fisiere de configurare)
Prelucrarea fisierelor YAML:
1. deserializare (citire):
    obiect = yaml.safe_load(file_object)
    transformarea fisierului YAML in obiecte specifice Python, dict, list etc
2. serializare (scriere in fisier YAML)
    yaml.dump(file_object)
Serializare si deserializare aplicate unui stream de tip string in loc de file
object:
    deserializare:
        obiect = yaml.load(string)
    serializare: 
       string = yaml.dump(obiect)
"""


import yaml
from yaml import Loader

with open('data\config.yaml', 'r') as f:
    data = yaml.safe_load(f)
    print(type(data))
    print(f'Deserealizarea a generat: {data}')
    print(f'Lista data_types: {data["data_types"]}')
    data["data_types"].append("tuple")
    print(f'Lista data_types dupa append: {data["data_types"]}')
    print(data)
print()
with open('data/config2.yaml', 'w+') as f:
    yaml.dump(data, f, default_flow_style=False)
    f.seek(0)
    for line in f:
        print(line, end='')
print()
course_yaml = """
    course: Python Developer
    tools: [Git, Visual Studio Code, GitHub]
"""
data_course = yaml.safe_load(course_yaml)
data_course2 = yaml.load(course_yaml, Loader=Loader)
print(type(data_course))
print(f'Deserializarea stringului a generat: {data_course}')
data_course["nr_studenti"] = 20
new_course_yaml = yaml.dump(data_course, default_flow_style=False)
print(f'Noul string YAML: \n{new_course_yaml}')