cities = {
    'fort wayne': {
        'country': 'united states of america',
        'population': '263,886',
        'fact': 'the city was named after general anthony wayne',
    },

    'detroit': {
        'country': 'united states of america',
        'population': '639,111',
        'fact': 'detroit used to be the car manufacturing hub of the whole world',
    },

    'chicago': {
        'country': 'united states of america',
        'population': '2,746,388',
        'fact': 'chicago is a pretty dangerous place at times',
    }
}

for city, information in cities.items():
    print(f"City: {city.title()}")
    print(f"Country: {information['country'].title()}")
    print(f"Population According to the 2020 United States Census: {information['population']}")
    print(f"One Fact About City: {information['fact'].title()}")
    print()
