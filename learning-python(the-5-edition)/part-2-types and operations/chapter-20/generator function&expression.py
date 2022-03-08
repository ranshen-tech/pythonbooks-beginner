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
