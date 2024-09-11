# People from 6.1
person_1 = {
    'first_name': 'jon',
    'last_name': 'becraft',
    'age': '17',
    'city': 'tanbark trails, Fort Wayne',
}

# The two more dictionary's
person_2 = {
    'first_name': 'quinn',
    'last_name': 'deshone',
    'age': '18',
    'city': 'junkyard avenue, Fort Wayne',
}

person_3 = {
    'first_name': 'daniel',
    'last_name': 'webber',
    'age': '17',
    'city': 'misty mountains, Fort Wayne',
}

person_4 = {
    'first_name': 'peyton',
    'last_name': 'moses',
    'age': '17',
    'city': 'sunny brook, Fort Wayne',
}

# The people list
people = [person_1, person_2, person_3, person_4]

for person in people:
    print(f"Name:{person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age:{person['age']}")
    print(f"City:{person['city'].title()}")
    print()