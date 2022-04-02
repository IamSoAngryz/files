"""
Python file handling (lucrul cu fisiere in Python)
Link documentatie oficiala: https://docs.python.org/3/library/io.html
Fisier = o locatie de pe disc, avand un nume asociat care este utilizata pentru
stocarea informatiei

Lucrul cu fisiere:
- deschiderea unui fisier
- citire si scriere din, respectivul fisier
- inchidere

Deschiderea unui fisier se realizeaza cu functia open.
Sintaxa:
f = open(nume_fisier, mod_deschidere)
unde f = stream / file handler (file object) care perimite accesul la informatia
din fisier (la continutul acestuia, permitand manevrarea continutului)
In cazul fisierelor text, streamul (manevrarea acestuia) intoarce si primeste obiecte de tip string
(siruri de caractere)
modul_deschidere poate fi:
- text (implicit) sau binar
- r (implicit) - citire sau alte caractere w, a, x, +
"""

f = open('date.txt', 'r')           # deschidere fisier, implicit pt citre
file_content = f.read()
print(file_content, end = ' ')      # citim din fisier si afisam
print(type(f))                      # _io.TextIOWrapper
print(type(file_content))           # str
f.close()                           # inchidem fisierul