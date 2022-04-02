"""
Delete files (stergerea fisierelor)
Modulul os (built-in)
    - lucrul cu fisiere din sistemul operare (operating system)
    os.listdir(folder) -returneaza o lista cu fisiere si foldere din folder
    os.getcwd()        -returneaza un string cu calea completa catre folderul
                        curent (inclusiv folderul curent)
    os.remove(fisier)  - sterge un fisier de pe disc daca exista
    os.path.exists(f)  - returneaza True daca fisierul f exista
    os.path.join(folder, file) - returneaza un string cu calea compusa din
                                folder si fisier (folder/fisier sau folder\fisier)
"""
import os


def delete_file(file):
    if os.path.exists(file):
        os.remove(file)
        print(f'Fisierul {file} a fost sters')
    else:
        print(f'Fisierul {file} nu exista pe disc')
# with open(file, 'w') as f:
#     pass        # truncate(stergerea continutului)


# print(dir(os))
print(os.getcwd())  # arata folderul curent
print(os.listdir())  # afiseaza continutul folderului
lista_foldere_fisiere = os.listdir()
for item in lista_foldere_fisiere:
    print(item)
print(f'Numarul de fisiere si foldere: {len(lista_foldere_fisiere)}')
try:
    os.remove('tari2.txt')
except FileNotFoundError as e:
    print(f'{e.__class__.__name__}: {e}')

# if os.path.exists('tari2.txt'):
#     os.remove('tari2.txt')
#     print('Fisierul a fost sters')
# else:
#     print('Fisierul nu exista pe disc')

delete_file('tari2.txt')
delete_file('testfolder/f.txt')
print(os.path.join('testfolder', 'g.txt'))
delete_file(os.path.join('testfolder', 'g.txt'))
# delete_file('testfolder/g.txt')