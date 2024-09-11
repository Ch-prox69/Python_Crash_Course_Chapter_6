# favorite places dictionary 
favorite_places = {
    'jon': ['tokyo buffet, fort wayne, indiana', 'fort wayne pinball, fort wayne, indiana'],
    'aiden': ['northrop wrestling room, fort wayne, indiana', 'home, fort wayne, indiana'],
    'peyton':['girlfriends house, fort wayne, indiana'],
    'mr.mckinstry':['wrigley field, chicago', 'fernandina beach, flordia'],
}

# Printing
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")