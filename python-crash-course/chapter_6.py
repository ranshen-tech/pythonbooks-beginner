# 6-1
person = {
    "first_name": "ran",
    "last_name": "shen",
    "age": 29,
    "city": "huai nan",
    }

print(person["first_name"])
print(person["last_name"])
print(person['age'])
print(person["city"])
print()


# 6-2
favourite_numbers = {
    'ranshen': 9,
    'zhuyucheng': 66,
    'xupeng': 23,
    'chenyuanyuan': 888,
    'zhoufan': 100_000,
    }

num = favourite_numbers['ranshen']
print(f"Ranshen's favourite number is {num}.")

num = favourite_numbers['zhuyucheng']
print(f"Zhuyucheng's favourite number is {num}.")

num = favourite_numbers['xupeng']
print(f"Xupeng's favourite number is {num}.")

num = favourite_numbers['chenyuanyuan']
print(f"Chenyuanyuan's favourite number is {num}.")

num = favourite_numbers['zhoufan']
print(f"Zhoufan's favourite number is {num}.")
print()


# 6-3
glossary = {
    "string": "A series of characters.",
    "comment": "A note in a program that the python interpreter ignores.",
    "list": "A collection of items in a particular order.",
    "loop": "Work through a collection of items, one at a time.",
    "dictionary": "A collection of key-value pairs.",
    }

word = 'string'
print(f"{word.title()}:\n\t{glossary[word]}")

word = 'comment'
print(f"\n{word.title()}:\n\t{glossary[word]}")

word = 'list'
print(f"\n{word.title()}:\n\t{glossary[word]}")

word = 'loop'
print(f"\n{word.title()}:\n\t{glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}:\n\t{glossary[word]}")


# 6-4
glossary = {
    "string": "A series of characters.",
    "comment": "A note in a program that the Python interpreter ignores.",
    "list": "A collection of items in a particular order.",
    "loop": "Work through a collection of items, one at a time.",
    "dictionary": "A collection of key-value pairs.",
    "key": "The first item in a key-value pair in a dictionary.",
    "value": "An item associated with a key in a dictionary.",
    "conditional test": "A comparison between two values.",
    "float": "A numerical value with a decimal component.",
    "boolean expression": "An expression that evaluates to True or False.",
    }

for key, value in glossary.items():
    print(f"\n{key.title()}:\n\t{value}")
print()


# 6-5
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")
print()

# 6-6
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
print('f\nf')