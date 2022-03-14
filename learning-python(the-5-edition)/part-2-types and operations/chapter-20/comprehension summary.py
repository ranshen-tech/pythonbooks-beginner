print([x * x for x in range(10)])

print((x * x for x in range(10)))

print({x * x for x in range(10)})

print({x: x * x for x in range(10)})
print("\n")


# action scope及推导变量

print(x for x in range(5))
print("\n")

x = 99
print([x for x in range(5)])
print(x)
print("\n")

y = 99
for y in range(5):
    pass
print(y)
print("\n")


x = "aaa"


def func():
    y = "bbb"
    print(z for z in x + y)
    print("".join(z for z in x + y))


func()
print("\n")

print(x for x in range(5))
print("\n")

x = 99
print([x for x in range(5)])

print(x)
print("\n")

y = 99
for y in range(5):
    pass
print(y)
print("\n")


# understand set-comprehension and dict-comprehension

print({x * x for x in range(10)})
print(set(x * x for x in range(10)))
print("\n")

print({x: x * x for x in range(10)})
print(dict((x, x * x) for x in range(10)))
print("\n")


res = set()
print(res)
for x in range(10):
    res.add(x * x)

print(res)
print(x)
print("\n")

res = {}
for x in range(10):
    res[x] = x * x

print(res)
print(x)
print("\n")


G = ((x, x * x) for x in range(10))
print(next(G))
print(next(G))
print("\n")


# set and dict's extended comprehension gramar

print([x * x for x in range(10) if x % 2 == 0])
print({x * x for x in range(10) if x % 2 == 0})
print({x: x * x for x in range(10) if x % 2 == 0})
print("\n")


print([x + y for x in [1, 2, 3] for y in [4, 5, 6]])
print({x + y for x in [1, 2, 3] for y in [4, 5, 6]})
print({x: y for x in [1, 2, 3] for y in [4, 5, 6]})
print("\n")


print({x + y for x in "ab" for y in "cd"})

print({x + y: (ord(x), ord(y)) for x in "ab" for y in "cd"})

print({k * 2 for k in ["spam", "ham", "sausage"] if k[0] == "s"})

print({k.upper(): k * 2 for k in ["spam", "ham", "sausage"] if k[0] == "s"})
