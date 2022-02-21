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

print([ord(c) for c in S])
print("\n")


# exercise2

for i in range(5):
    print("hello %d\n\a" % i)
print("\n")


# exercise3

D = {"b": 2, "a": 1, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7}
keys = list(D)
print(keys)
keys.sort()
for key in keys:
    print(key, "=>", D[key])
print("\n")

for key in sorted(D):
    print(key, "=>", D[key])
print("\n")

import power
