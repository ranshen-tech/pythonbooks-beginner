import json

try:
    with open('favourite_number.json') as f:
        favourite_number = json.load(f)
except FileNotFoundError:
    pass
else:
    print(f"I know your favourite number, It's {favourite_number}")

# favourite_number = input("What your favourite number? ")
# with open('favourite_number.json', 'w') as f:
#     json.dump(favourite_number, f)
# print(f"Thanks, I'll remember that.")
