"""
Uniformizarea unui dictionar nested
"""
import pprint   # pretty print

nested_dict ={
         'name': 'John Doe',
        'age': 20,
        'address':{
            'street': 'The Street',
            'number': 20
        },
        'salary': 2500    

}
flat_dict = dict()
for key, value in nested_dict.items():
    if type(value) is dict:
        for inside_key, inside_value in value.items():
            flat_dict['.'.join((key, inside_key))] = inside_value
    else:
        flat_dict[key] = value
print(f'Dictionarul initial, nested: {nested_dict}')
print(f'Dictionarul initial, flattened: {flat_dict}')

pprint.pprint(nested_dict, width=60, indent=4)
pprint.pprint(flat_dict, width=60, indent=4)