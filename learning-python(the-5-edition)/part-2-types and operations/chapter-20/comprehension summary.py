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
