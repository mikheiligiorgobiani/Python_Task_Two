students = [
    {
        'name': 'Nick',
        'age': 22,
        'address': {
            'country': 'Georgia',
            'city': 'Tbilisi',
            'streed': '1st street'
        },
    },
    {
        'name': 'Mary',
        'age': 27,
        'address': {},
        'subjects': ['Math', 'Linux', 'Networking']
    },
    {
        'name': 'Josh',
        'age': 23,
        'address': {},
        'subjects': ['Biology', 'Chemistry']
    },
    {
        'name': 'James',
        'age': 19,
        'subjects': [],
        'address': {
            'country': 'Georgia',
            'city': 'Tbilisi',
            'streed': '1st street'
        }
    }
]

for student in students:
    print('-' * 10)
    print(student['name'])
    address = student.get('address')
    subjects = student.get('subjects')
    if address:
        print(address['city'])

    if subjects:
        print(subjects[0])
