"""
Write / Create files
(Scrierea in fisiere / Crearea fisierelor)

Scrierea in fisiere se realizeaza prin deschiderea in modul scriere
 w  - scriere, cu posibilitatea de suprascriere daca fisierul exista
    - daca nu exista fisierul, este creat
 a  - adaugare la sfarsitul fisierului(append)
 x  - crearea fisierului
 +  - folosit cu r sau w sau a perimite atat scriere cat si citire

Metoda write() permite scrierea efectiva a unui sir de caracter
Sintaxa:
f.write(sir_de_caractere
Pentru diferentierea pe linii a continutului scirs este aduagat implicit
'\n' -newline
"""

with open('orase.txt', 'w') as f:
    f.write('Barcelona, Spania\n')
    f.write('Paris, Franta\n')
    f.write('Londra, UK\n')
    f.seek(0)
    # print(f.read())
    

# with open('orase.txt', 'r') as f:
#     # print(f.read(), end='')
#     for line in f:
#         print(line, end = '')

with open('orase.txt', 'w+') as f:
    f.write('Oradea, Romania\n')
    f.write('Bacau, Romania\n')
    f.seek(0)
    for line in f:
        print(line, end='')
print()
with open('orase.txt', 'a+') as f:
    f.write('Berlin, Germania\n')
    f.seek(0)
    for line in f:
        print(line, end='')
print()
with open('tari2.txt', 'x+') as f:
    print(f.tell())
    f.write('Franta\n')
    f.seek(0)
    for line in f:
        print(line, end='')
print()
with open('orase3.txt', 'a+') as f:
    f.write('test\n')