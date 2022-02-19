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
