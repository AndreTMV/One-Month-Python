# states = ['NY', 'PA', 'CA']
# states = ['New York', 'Pennsylvania', 'California']

# Dictionaries
states = {'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California'}

# Accesing data in dictionaries
print(states['NY'])

# print(states['FL'])

people = ['Andre', 'Fulano']
print(type(states))
print(type(people))

print(states.get('FL', 'Not found'))
print(states.get('NY', 'Not found'))

print(states.keys())
print(states.values())

# New key-value pair
states['FL'] = 'Florida'
print(states)

animal_sounds = {
    "cat": ['mew', 'purf'],
    "dog": ["woof", "bark"],
    "fox": []
}

Andre = {'name': 'Andre', 'height': 6,
         'shoe size': 28, 'hair': 'brown', 'eyes': 'brown'}

Isis = {'name': 'Isis', 'height': 5.6,
        'shoe size': 25, 'hair': 'brown', 'eyes': 'brown'}

Tere = {'name': 'Tere', 'height': 5.6,
        'shoe size': 23, 'hair': 'brown', 'eyes': 'brown'}
people2 = [Andre, Isis, Tere]

for person in people2:
    print(f"{person.get('name')} height is {person.get('height','Not found')}")
