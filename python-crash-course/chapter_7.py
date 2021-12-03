# # 7-1
# car = input("What kind of car would you like? ")

# print(f"Let me see if I can find you a {car.title()}.")


# # 7-2
# party_size = input("How many people are in your dinner party tonight? ")
# party_size = int(party_size)

# if party_size > 8:
#     print("I'm sorry, you'll have to wait for a table.")
# else:
#     print("Your table is ready.")


# # 7-3
# number = input("Give me a number, please: ")
# number = int(number)

# if number % 10 == 0:
#     print(f"{number} is a multiple of 10.")
# else:
#     print(f"{number} is not a multiple of 10.")


# 7-4
# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "

# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"- I'll add {topping} to your pizza.")
#     else:
#         break


# 7-5
# prompt = "How old are you?"
# prompt += "\nEnter 'quit' when you are finished. "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)
#     if age < 3:
#         print("You get in free!")
#     elif age < 13:
#         print("Your ticket is $10.")
#     else:
#         print("Your ticket is $15.")


# 7-8
# sandwich_orders =['veggie', 'grilled cheese', 'turkey', 'roast beef']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I'm working on your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print()
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich} sandwich.")
# print('\n')


# # 7-9
# sandwich_orders = [
#     'pastrami', 'veggie', 'grilled cheese', 'pastrami',
#     'turkey', 'roast beef', 'pastrami'
#     ]
# finished_sandwiches = []

# print("I'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print()
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I'm working on your {current_sandwich} sandwich.")
#     finished_sandwiches.append(current_sandwich)
# print()
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich} sandwich.")
# print('\n')


# 7-10
name_prompt = "\nWhat's your name? "
place_prompt = 'If you could visit one place in the world,'
place_prompt += 'where would you go? '
continue_prompt = 'Would you like to let someone else respond? (yes/no) '

responds = {}

while True:
    name = input(name_prompt)
    place = input(place_prompt)
    responds[name] = place
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break
    
print("\n--- Result ---")
for name, place in responds.items():
    print(f"{name.title()} would like to visit {place.title()}.")