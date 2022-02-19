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

for (a, b), c in [((1, 2), 3), ((4, 5), 6)]:
    print(a, b, c)
print("\n")

for (a, b), c in [([1, 2], 3), ["XY", 6]]:
    print(a, b, c)
print("\n")


# Python 3.X entended sequence assignment in the for loop
a, b, c = (1, 2, 3)
print(a, b, c)
print("\n")

for a, b, c in [(1, 2, 3), (4, 5, 6)]:
    print(a, b, c)
print("\n")

a, *b, c = (1, 2, 3, 4)
print(a, b, c)
print("\n")

for a, *b, c in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)
print("\n")

for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = all[0], all[1:3], all[3]
    print(a, b, c)
print("\n")


# Nested in the for loop
items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found!")
print("\n")

for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key, "not found!")
print("\n")

seq1 = "spam"
seq2 = "scam"

res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)
print("\n")

print([x for x in seq1 if x in seq2])
print("\n")


# Be careful: file scanner

file = open("data.txt")
print(file.read())
print("\n---------------")

file = open("log.txt")
while True:
    char = file.read(2)
    if char:
        print(char)
    else:
        break
print("\n------------")

for char in open("log.txt").read():
    print(char)
print("\n------------")

file = open("log.txt")
while True:
    line = file.readline()
    if line:
        print(line.rstrip())
    else:
        break
print("\n")

file = open("log.txt", "rb")
while True:
    chunk = file.read()
    if not chunk:
        break
    print(chunk)
print("\n")

for line in open("log.txt").readlines():
    print(line.rstrip())
print("\n-----------------")

for line in open("log.txt"):
    print(line.rstrip())
print("\n")

for line in reversed(open("log.txt").readlines()):
    print(line)
print("\n")

print(type(open("log.txt").read()))
