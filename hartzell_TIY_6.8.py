pet_1 = {
    'animal': 'black labrador',
    'owner': 'christopher hartwell',
}

pet_2 = {
    'animal': 'cat',
    'owner': 'larry bird'
}

pet_3 = {
    'animal': 'gerbil',
    'owner': 'scary garry'
}

# pet list
pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Pet: {pet['animal'].title()}")
    print(f"Owner: {pet['owner'].title()}")
    print()
