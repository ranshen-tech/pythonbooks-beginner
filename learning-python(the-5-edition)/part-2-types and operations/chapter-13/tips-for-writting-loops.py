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
