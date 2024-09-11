# Names and Numbers
names_and_numbers = {
    'jon': ['69', '420'],
    'daniel': ['45', '53'],
    'peyton': ['16', '2'],
    'quinn': ['99', '47'],
    'jacob': ['44', '65'],
}

# Printing
for name, numbers in names_and_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
            print(f"\t{number}")