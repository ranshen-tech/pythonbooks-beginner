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
print("\n💖")

print([line.upper() for line in open("script2.py")])
print("\n")

print([line.rstrip().upper() for line in open("script2.py")])
print("\n")

print([line.split() for line in open("script2.py")])
print("\n")

print([line.replace(" ", "!") for line in open("script2.py")])
print("\n")

print([("sys" in line, line[:5]) for line in open("script2.py")])
print("\n")


# Extended list-comprehension syntax
# 筛选分句：if

lines = [line.rstrip() for line in open("script2.py") if line[0] == "p"]
print(lines)
print("\n")

res = []
for line in open("script2.py"):
    if line[0] == "p":
        res.append(line.rstrip())
print(res)
print("\n")


# 嵌套循环：for
