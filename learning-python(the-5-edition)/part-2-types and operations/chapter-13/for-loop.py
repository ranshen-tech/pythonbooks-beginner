# Example

for x in ["spam", "eggs", "ham"]:
    print(x, end=" ")
print("\n")

sum = 0
for x in [1, 2, 3, 4]:
    sum += x
print(sum)

prod = 1
for item in [1, 2, 3, 4]:
    prod *= item
print(prod)
print("\n")


# Other data types

S = "lumberjack"
T = ("and", "I'm", "okay")

for x in S:
    print(x, end=" ")
print("\n")

for x in T:
    print(x, end=" ")
print("\n")


# Tuple assignment in the for loop

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)
print("\n")

D = {"a": 1, "b": 2, "c": 3}
for key in D:
    print(key, "=>", D[key])
print("\n")

print(list(D.items()))
print("\n")

for key, value in D.items():
    print(key, "=>", value)
print("\n")

print(T)
print("\n")

for both in T:
    a, b = both
    print(a, b)
print("\n")

((a, b), c) = ((1, 2), 3)
print(a, b, c)
print("\n")
