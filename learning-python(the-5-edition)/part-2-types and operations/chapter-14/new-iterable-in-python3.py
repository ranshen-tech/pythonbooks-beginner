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

print(filter(bool, ["spam", "", "ni"]))
print(list(filter(bool, ["spam", "", "ni"])))
print("\n")

print([x for x in ["spam", "", "ni"] if bool(x)])
print([x for x in ["spam", "", "ni"] if x])
print("\n")


# Multiple-iterators vs Single-pass-iterators

R = range(3)
# print(next(R))

I1 = iter(R)
print(next(I1))
print(next(I1))
I2 = iter(R)
print(next(I2))
print(next(I1))
print("\n")

Z = zip((1, 2, 3), (10, 11, 12))
I1 = iter(Z)
I2 = iter(Z)
print(next(I1))
print(next(I1))
print(next(I2))
print("\n")

M = map(abs, (-1, 0, 1))
I1 = iter(M)
I2 = iter(M)
print(next(I1), next(I1), next(I1))
# print(next(I2))
print("\n")

R = range(3)
I1, I2 = iter(R), iter(R)
print([next(I1), next(I1), next(I1)])
print(next(I2), next(I2))
print("\n")


# Dictionary view iterable

D = dict(a=1, b=2, c=3)
print(D)

K = D.keys()
print(K)
# print(next(K))
I = iter(K)
print(next(I))
print(next(I))
for k in D.keys():
    print(k, end=" ")
print("\n")

K = D.keys()
print(list(K))

V = D.values()
print(V)
print(list(V))
# print(V[0])
print(list(V)[0])
print(list(D.items()))
for k, v in D.items():
    print(k, v, end=" ")
print("\n")

print(D)
I = iter(D)
print(next(I))
print(next(I))
for key in D:
    print(key, end=" ")
print("\n")

print(D)
print(sorted(D.keys()))
for k in sorted(D.keys()):
    print(k, D[k], end=" ")
print("\n")

for k in sorted(D):
    print(k, D[k], end=" ")
print("\n")
