"""
XML file (Fisier XML)
XML     - eXtensible Markup Language
        - format de interschimabre a datelor in care informatia este
        organizata ierarhic, intr-un arbore (tree) cu elemente caracterizate
        de un tag (eticheta) si atribute
        - are un root (radacina)
Modulul xml permite prelucrarea fisierelor XML
Un obiect din clasa ElementTree este intreg documentul XML
Elementele sunt de tipul xml.etree.ElementTree.Element
"""

from xml.etree import ElementTree

tree = ElementTree.parse('data/countries.xml')
print(type(tree))
root = tree.getroot()
print(type(root))   # xml.etree.ElementTree.Element
print(f'Elementul root: {root} {root.tag}')
country_elemets = tree.findall("country")
print(f'Lista de elemente de tip country: {country_elemets}')
for element in country_elemets:
        # print(element)
        print(f'Tag: {element.tag}')
        print(f'Atribute: {element.attrib}')
        print(element.attrib['name'], end=' ')
        year = element.find('year')
        print(f'Anul: {year.text}')