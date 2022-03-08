# 内置类型、工具和类中的值生成

D = {"a": 1, "b": 2, "c": 3}
x = iter(D)
print(next(x))
print(next(x))
print(next(x))
print("\n")


for key in D:
    print(key, D[key])
print("\n")


for line in open("temp.txt"):
    print(line, end="")
print("\n")


# 生成器和库工具： 目录遍历器

import os

for (root, subs, files) in os.walk("."):
    for name in files:
        if name.startswith("call"):
            print(root, name)
print("\n")


G = os.walk(r"C:\code\pkg")
print(iter(G) is G)
I = iter(G)
# print(next(I))
print("\n")


# 生成器和函数应用


def f(a, b, c):
    print("%s, %s, and %s" % (a, b, c))


f(0, 1, 2)
f(*range(3))
f(*(i for i in range(3)))
print("\n")


D = dict(a="Bob", b="dev", c=40.5)
print(D)
f(a="Bob", b="dev", c=40.5)
f(**D)
f(*D)
f(*D.values())
print("\n")


for x in "spam":
    print(x.upper(), end=" ")
print("\n")

print(x.upper() for x in "spam")
print(list(print(x.upper(), end=" ") for x in "spam"))
print("\n")


# prepare: a user-defined iterable in class


class SomeIterable:
    def __init__(self):
        pass

    def __next__(self):
        pass
