L = [1, 2, 4, 8, 16, 32, 64]
X = 5

# a

i = 0
while i < len(L):
    if 2**X == L[i]:
        print("at index", i)
        break
    i += 1
else:
    print(X, "not found")
print("\n")

# b

for num in L:
    if 2**X == num:
        print(2**X, "was found at", L.index(num))
        break
else:
    print(X, "not found")
print("\n")

# c

if 2**X in L:
    print(2**X, "was found at", L.index(2**X))
else:
    print(X, "not found")
print("\n")

# d

X = 5
L = []
for i in range(7):
    L.append(2**i)
print(L)
print("\n")

# e

if 2**X in L:
    print(2**X, "was found at", L.index(2**X))
else:
    print(X, "not found")
print("\n")

# f

L = list(map(lambda x: 2**x, range(7)))
print(L)

if 2**X in L:
    print(2**X, "was found at", L.index(2**X))
else:
    print(X, "not found")
print("\n")
