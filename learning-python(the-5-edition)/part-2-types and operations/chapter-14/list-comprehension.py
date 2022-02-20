L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10
print(L)
print("\n")

L = [x + 10 for x in L]
print(L)
print("\n")


# List comprehension basics

res = []
for x in L:
    res.append(x + 10)
print(res)
print("\n")


# Use list-comprehension on files

f = open("script2.py")
lines = f.readlines()
print(lines)
print("\n")

lines = [line.rstrip() for line in lines]
print(lines)
print("\n")

lines = [line.strip() for line in open("script2.py")]
print(lines)
print("\n")
