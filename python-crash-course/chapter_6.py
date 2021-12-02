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

languages = ['python', 'c', 'c', 'ruby']

print(set(languages))