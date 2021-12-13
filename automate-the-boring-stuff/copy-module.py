import copy

spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

x = ['a', ['b', 'c'], 'e']
apple = copy.deepcopy(x)
apple[0] = 1
orange = copy.copy(x)
orange[0] = 1
print(x)
print(orange)
print(x)
print(apple)