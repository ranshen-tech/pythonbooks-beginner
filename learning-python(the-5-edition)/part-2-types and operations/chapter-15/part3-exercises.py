# exercise1
S = "spam"
for c in S:
    print(ord(c))
print("\n")

x = 0
for c in S:
    x += ord(c)
print(x)
print("\n")

x = []
for c in S:
    x.append(ord(c))
print(x)
print("\n")

print(list(map(ord, S)))
print("\n")
