# application of generator functions


def gensquares(N):
    for i in range(N):
        yield i**2


for a in gensquares(5):
    print(a, end=" : ")
print("\n")

x = gensquares(4)
print(x)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print("\n")

y = gensquares(5)
print(iter(y) is y)
print(next(y))
print(next(y))
print("\n")


# 为什么要使用generator function


def buildsquares(n):
    res = []
    for i in range(n):
        res.append(i**2)
    return res


for x in buildsquares(5):
    print(x, end=" : ")
print("\n")

for x in [n**2 for n in range(5)]:
    print(x, end=" : ")
print("\n")

for x in map(lambda n: n**2, range(5)):
    print(x, end=" : ")
print("\n")


def ups(line):
    for sub in line.split(","):
        yield sub.upper()


print(tuple(ups("aaa,bbb,ccc")))
print({i: s for i, s in enumerate(ups("aaa,bbb,ccc"))})
print("\n")


# 扩展生成器函数协议：send VS next


def gen():
    for i in range(10):
        X = yield i
        print(X)


G = gen()
print(next(G))
print(G.send(77))
print(G.send(88))
print(next(G))
print("\n")


# 生成器表达式：当可迭代对象遇见推导语法

print([x**2 for x in range(4)])
print(x**2 for x in range(4))
print((x**2 for x in range(4)))

print(list(x**2 for x in range(4)))
print("\n")


G = (x**2 for x in range(4))
print(G)
print(iter(G))
print(iter(G) is G)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(G)
print("\n")


for num in (x**2 for x in range(4)):
    print("%s, %s" % (num, num / 2.0))
print("\n")


print("aaa,bbb,ccc".split(","))
print("".join(x.upper() for x in "aaa,bbb,ccc".split(",")))

a, b, c = (x + "\n" for x in "aaa,bbb,ccc".split(","))
print(a, c)
print("\n")


print(sum(x**2 for x in range(4)))
print(sorted(x**2 for x in range(4)))
print(sorted((x**2 for x in range(4)), reverse=True))
print("\n")


# Why use generator expression
# generator expression VS map

print(list(map(abs, (-1, -2, 3, 4))))
print(list(abs(x) for x in (-1, -2, 3, 4)))
print(list(map(lambda x: x * 2, (1, 2, 3, 4))))
print(list(x * 2 for x in (1, 2, 3, 4)))
print("\n")


line = "aaa,bbb,ccc"
print(x.upper() for x in line.split(","))
print("".join([x.upper() for x in line.split(",")]))

print("".join(x.upper() for x in line.split(",")))
print("".join(map(str.upper, line.split(","))))

print("".join(x * 2 for x in line.split(",")))
print("".join(map(lambda x: x * 2, line.split(","))))
print("\n")


print([x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]])

print(list(map(lambda x: x * 2, [abs(x) for x in (-1, -2, 3, 4)])))
print(list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))))

print(list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))))
print("\n")


import math

print(list(map(math.sqrt, (x**2 for x in range(4)))))
print("\n")

print(list(map(abs, map(abs, map(abs, (-1, 0, 1))))))
print(list(abs(x) for x in (abs(x) for x in (abs(x) for x in (-1, 0, 1)))))
print("\n")


print(list(abs(x) * 2 for x in (-1, -2, 3, 4)))
print(list(math.sqrt(x**2) for x in range(4)))
print(list(abs(x) for x in (-1, 0, 1)))
print("\n")


# generator expression VS filter

line = "aa bbb c"
print("".join(x for x in line.split() if len(x) > 1))
print("".join(filter(lambda x: len(x) > 1, line.split())))
print("\n")

for x in line.split():
    if len(x) > 1:
        print(x)
print("\n")


print("".join(x.upper() for x in line.split() if len(x) > 1))
print("".join(map(str.upper, filter(lambda x: len(x) > 1, line.split()))))
print("\n")


print("".join(x.upper() for x in line.split() if len(x) > 1))

res = ""
for x in line.split():
    if len(x) > 1:
        res += x.upper()

print(res)
print("\n")


# generator function VS generator expression

G = (c * 4 for c in "SPAM")
print(G)
print(list(G))
