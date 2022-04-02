"""
Read files (Citirea fisierelor)
Sintaxa:
f = open(nume_fisier, 'rt')
f = open(nume_fisier)
Modul implicit de deschidere a unui fisier cu open este read (citire) si tipul
implicit este t (text)
Context manager with -as este o practicata recomandata in lucrul cu fisiere,
avantajul fiind ca grupeaza blocul de instructiuni care manevreaza continutul
(obiectul de tip fisier) si inchiderea fisirului se face automat.
Sintaxa:
with open(nume_fisier, mod_deschidere) as f:
    intructiuni

Citirea se realizeaza:
read(size) - citirea continutului(in totalitate sau in bucati de dimensiune
                size -numarul de caractere de citit) si returneaza un string
readlines() - o lista cu liniile (sitringuri) din fisier, inclusiv newline '\n'
readline() - citirea pana intalneste newline sau EOF
tell()    - pozitia in fisier ( pozitia cursorului)
seek(pozitie)   - pozitioneaza cursorul in fisier

"""
f = open('date.txt')
print(f.read(), end='')
f.close()

with open('date.txt') as f:
    print(f.read(), end='')

with open('date.txt') as f:
    file_content = f.readlines()
    print(file_content)

with open('date.txt', 'r') as f:
    for line in f.readlines():
        print(line, end='')

with open('date.txt', 'r') as f:
    for line in f:
        print(line, end ='')

with open('orase.txt', 'r') as f:
    size_to_read = 5
    content = f.read(size_to_read)
    while len(content) > 0: # citirea din fisier a intors un string cu dim > 0
        print(content, end='')
        content = f.read(size_to_read)

try:
    with open('orase2.txt', 'r') as f:
        print(f.readline(), end = '')
        print(f.readline(), end = '')
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')

try:
    with open('orase.txt', 'r', encoding='utf-8') as f:
        print(f.readline(), end = '')
        print(f.readline(), end = '')
        print(f'Pozitia in fisier: {f.tell()}')
        f.seek(0)
        print(f.readline(), end = '')
        # f.seek(2)
        print(f.readline(), end = '')
        print(f.readline(), end = '')
        print(f.readline(), end = '')
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')
print(f)
print(f.name)
print(f.mode)
print(f.closed)

# f.read()