programming_words = {
    'list': 'Collection of items in a strict order',
    'value': 'A letter or number in a program',
    'boolean': 'A value that is either true or false',
    'string': 'A series of characters',
    'dictionary': 'A collection of key-value pairs',
    'keys': 'Indexes of a list',
    'function': 'A reusable block of code that preforms a specific task and can return a result',
    'variable': 'A named storage location in memory that holds a value which can be changed during program execution',
    'loop': 'A control structure that repeatedly executes a block of code as long as the specified condition is true',
    'class': 'A blueprint for creating objects, defining the properties and behaviors in object-oriented programming',

}

# Sorting the keys
sorted_keys = sorted(programming_words.keys())

# Printing
for word in sorted_keys:
    meaning = programming_words[word]
    print(f"{word.title()}:")
    print(f"{meaning.title()}\n")
