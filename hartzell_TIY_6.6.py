favorite_langueges = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# List of people who need to take the poll
people_list = ['jack', 'jen', 'brady', 'edward']

for people in people_list:
    if people in favorite_langueges:
        print(f"Dear {people.title()}, thank you for taking the poll\n")
    else:
        print(f"Dear {people.title()}, you are invited to take the poll")