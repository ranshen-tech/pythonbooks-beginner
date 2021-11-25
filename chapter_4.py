# 4-1
favourite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
# 打印所有pizza的名称
for pizza in favourite_pizzas:
    print(pizza)

print('\n')

# 针对每种pizza打印一个句子
for pizza in favourite_pizzas:
    print(f"I like {pizza} pizza!")

print("\nI really love pizza!")


# 4-3
numbers = list(range(1, 21))

for number in numbers:
    print(number)


# 4-5
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))


# 4-7
threes = list(range(3, 31, 3))

for number in threes:
   print(number)


# 4-8
cubes = []
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)


# 4-9
cubes = [number ** 3 for number in range(1, 11)]

for cube in cubes:
    print(cube)


# 4-11
favourite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favourite_pizzas[:]

favourite_pizzas.append("meat lover's")
friend_pizzas.append('pesto')

print("\nMy favourite pizzas are:")
for pizza in favourite_pizzas:
    print(f"- {pizza}")

print("\nMy friend favourite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")


# 4-13
menu_items = ('beef', 'chicken', 'apple', 'orange', 'egg',)

print("\nYou can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")

menu_items = ('beef', 'chicken', 'apple', 'milk', 'water',)

print("\nOur menu has been updated.")
print("You can now choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")