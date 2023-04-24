# 6-1
person = {
    "first_name": 'misho',
    "last_name": 'giorgobiani',
    "age": 22,
    "city": 'kutaisi'
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6-2
favorite_numbers = {
    "Giga": 5,
    "Giorgi": 3,
    "Misho": 7,
    "Oto": 1000_000,
    "Anri": 9
}
num = favorite_numbers['Giga']
print(f"Giga's favorite number is {num}.")

num = favorite_numbers['Giorgi']
print(f"Giorgi's favorite number is {num}.")

num = favorite_numbers['Misho']
print(f"Misho's favorite number is {num}.")

num = favorite_numbers['Oto']
print(f"Oto's favorite number is {num}.")

num = favorite_numbers['Anri']
print(f"Anri's favorite number is {num}.")

# 6-3
glossary = {
    'list' : 'A collection of items in a particular order',
    'string': 'A series of characters',
    'dictionary': 'A collection of key-value pairs',
    'key': 'The first item in a key-value pair in a dictionary',
    'float': 'A numerical value with a decimal component'
}