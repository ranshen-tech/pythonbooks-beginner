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
