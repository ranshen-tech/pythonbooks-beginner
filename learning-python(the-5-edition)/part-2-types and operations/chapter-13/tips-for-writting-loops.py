# Counter cycle: range

print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
print("\n")

print(list(range(-5, 5)))
print("\n")

print(list(range(5, -5, -1)))
print("\n")

for i in range(3):
    print(i, "Pythons")
print("\n")


# Sequence scan: while and range vs for

X = "spam"
for item in X:
    print(item, end=" ")
print("\n")

i = 0
while i < len(X):
    print(X[i], end=" ")
    i += 1
print("\n")

print(X)
print(len(X))
print(list(range(len(X))))
for i in range(len(X)):
    print(X[i], end=" ")
print("\n")

for item in X:
    print(item, end=" ")
print("\n")


# Sequence sequencer: range and len

S = "spam"
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=" ")
print("\n")

print(S)
for i in range(len(S)):
    X = S[i:] + S[:i]
    print(X, end=" ")
print("\n")

L = [1, 2, 3]
for i in range(len(L)):
    X = L[i:] + L[:i]
    print(X, end=" ")
print("\n")


# 非穷尽遍历：range VS slice

S = "abcdefghijk"
print(list(range(0, len(S), 2)))
print("\n")

for i in range(0, len(S), 2):
    print(S[i], end=" ")
print("\n")

S = "abcdefghijk"
for c in S[::2]:
    print(c, end=" ")
print("\n")


# 修改list：range vs 推导

L = [1, 2, 3, 4, 5]
for x in L:
    x += 1
print(L)
print(x)
print("\n")

L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 1
print(L)
print("\n")

i = 0
while i < len(L):
    L[i] += 1
    i += 1
print(L)

print([x + 1 for x in L])
print("\n")


# 并行遍历： zip and map

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
print(list(zip(L1)))
print(list(zip(L1, L2)))
print("\n")

for x, y in zip(L1, L2):
    print(x, y, "--", x + y)
print("\n")

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(T3)
print(list(zip(T1, T2, T3)))
print("\n")
