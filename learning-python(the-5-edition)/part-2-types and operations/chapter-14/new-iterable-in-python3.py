print(zip("abc", "xyz"))
print(list(zip("abc", "xyz")))
print("\n")

Z = zip((1, 2), (3, 4))
print(*Z)
print("\n💖")

M = map(lambda x: 2**x, range(3))
for i in M:
    print(i)
for i in M:
    print(i)
print("\n")


# range(iterable)

R = range(10)
print(R)
I = iter(R)
print(next(I))
print(next(I))
print(next(I))
print(list(range(10)))
print("\n")

print(len(R))
print(R[0])
print(R[-1])
print(next(I))
print(I.__next__())
print("\n")


# map & zip & filter (iterable)

M = map(abs, (-1, 0, 1))
print(M)
print(next(M))
print(next(M))
print(next(M))

for x in M:
    print(x)
print("\n")

M = map(abs, (-1, 0, 1))
for x in M:
    print(x)

print(list(map(abs, (-1, 0, 1))))
print("\n")

Z = zip((1, 2, 3), (10, 20, 30))
print(Z)
print(list(Z))

for pair in Z:
    print(pair)

Z = zip((1, 2, 3), (10, 20, 30))
print(next(Z))
print(next(Z))
print("\n")
