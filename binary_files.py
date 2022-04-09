"""
Binary files (fisiere binare)
Fisier binar    = un fisier care nu este text (nu este structurat pe linii
                terminate cu newline)
                = un fisier intr-un format care trebuie interpretat de o 
                aplicatie sau echipament hardware
                - contine si alte simboluri pe langa caractere si newlines
Pentru a lucra fisiere binare scriem si citim bytes.
Deschiderea fisierelor binare se realizaeaza cu modul "b"
"""

with open('data/ctrln.jpg', 'rb') as f:
    for line in f:
        print(line)
# realizarea unei copii a unui fisier binar
with open('data/ctrln.jpg', 'rb') as source_file:
    with open('data/ctrln_copy.jpg', 'wb') as destination_file:
        section_size = 1024
        section = source_file.read(section_size)
        while len(section) > 0:
            print(section)
            destination_file.write(section)
            section = source_file.read(section_size)