# lambda expression basis

# lambda argument1, argument2, ...argumentN: expression using arguments


def func(x, y, z):
    return x + y + z


print(func(2, 3, 4))
print("\n")

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))
print("\n")

x = lambda a="fee", b="fie", c="foe": a + b + c
print(x("wee"))
print(x())
print(x("ranshen", "good", "luck"))
print("\n")


def knights():
    title = "Sir"
    action = lambda x: title + " " + x
    return action


act = knights()
msg = act("robin")
print(msg)
print(act)
print("\n")


# 为什么使用lambda


L = [lambda x: x**2, lambda x: x**3, lambda x: x**4]

for f in L:
    print(f(2))

print(L[0](3))
print("\n")


def f1(x):
    return x**2


def f2(x):
    return x**3


def f3(x):
    return x**4


L = [f1, f2, f3]

for f in L:
    print(f(2))

print(L[0](3))
print("\n")


# 多分支switch语句：尾声


key = "got"
print({"already": lambda: 2 + 2, "got": lambda: 2 * 4, "one": lambda: 2**6}[key]())
print("\n")


def f1():
    return 2 + 2


def f2():
    return 2 * 4


def f3():
    return 2**6


key = "one"
print({"already": f1, "got": f2, "one": f3}[key]())
print("\n")


# 如何（不）让Python代码变得晦涩难懂

# if a:
#     b
# else:
#     c

# b if a else c

lower = lambda x, y: x if x < y else y
print(lower("bb", "aa"))
print(lower("aa", "bb"))
print("\n")


import sys

showall = lambda x: list(map(sys.stdout.write, x))
t = showall(["spam\n", "toast\n", "eggs\n"])
print("\n")

showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(("bright\n", "side\n", "of\n", "life\n"))
print("\n")

showall = lambda x: [print(line, end="\n") for line in x]
showall(("bright", "side", "of", "life"))
print("\n")

showall = lambda x: print(*x, sep="\n", end="\n")
showall(("bright", "side", "of", "life"))
