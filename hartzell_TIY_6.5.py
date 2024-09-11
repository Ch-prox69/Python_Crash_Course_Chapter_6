favorite_rivers = {
    'st. joseph river': 'fort wayne, indiana, united states of america',
    'amazon river': 'south america',
    'the nile river': 'egypt',
}

# Sorting the keys
sorted_rivers = sorted(favorite_rivers.items())

# Printing
for river, country in favorite_rivers.items():
    print(f"The river {river.title()} runs through {country.title()}")
    print()
    print(f"The river listed in this dictionary is the {river.title()}")
    print()
    print(f"The country where this river is located is {country.title()}")
    print()


