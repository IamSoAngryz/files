"""
Pickle  = Python object serialization
        = un modul dedicat serializarii / deserializarii obiectelor din Python
Pickling (Serialization / Scriere in fisier a unui stream de bytes)
    - procesul de conversie a unui obiect Python intr-un stream de bytes
    pickle.dump(obiect_Python, file_object)
Un-pickling (Deserialization / Citire)
    - procesul prin care un stream de bytes (dintr-un fisier binar sau un obiect
    bytes- like) este transformat intr-un obiect Python
    pickle.load(file_object)
"""

import pickle


class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f'Student: {self.name}')

pickle_stream = pickle.dumps(Student('John Doe'))       # pickle_stream - bytes
print(type(pickle_stream))
new_student = pickle.loads(pickle_stream)               # tip Student
print(type(new_student))
new_student.display()

with open('data/pickle_test.bin', 'wb') as f:
    pickle.dump(new_student, f)

with open('data/pickle_test.bin', 'rb') as f:
    python_object = pickle.load(f)
    print(type(python_object))
    print(python_object)