# Dictionary from fav lan example, but with added names
favorite_languages = {
    'jen': 'python',
    'sarah': 'c++',
    'edward': 'rust',
    'phil': 'python',
    'alice': 'java',
    'bob': 'javascript',
    'carol': 'ruby'
}

# List of people from list with added people 
people = ['jen', 'sarah', 'brady', 'edward', 'jack', 'phil', 'alice', 'mckinstry', 'bob', 'carol', 'dave']

# Decided to sort this and make it more appealing
sorted_people = sorted(people)
        
# Printing each person's favorite language
for person in sorted_people:
    language = favorite_languages.get(person.lower(), "not found")
    print()
    if language != "not found":
        print(f"{person.title()}'s favorite language is {language.title()}.")
    else:
        print(f"\tWe don't know what {person.title()}'s favorite language is.")