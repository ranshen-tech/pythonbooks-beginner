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

print([x + y for x in "abc" for y in "lmn"])
print("\n")

res = []
for x in "abc":
    for y in "lmn":
        res.append(x + y)
print(res)
print("\n")


# Other iteration contexts
for line in open("script2.py"):
    print(line.upper(), end="")
print("\n")

uppers = [line.upper() for line in open("script2.py")]
print(uppers)
print("\n")

print(list(map(str.upper, open("script2.py"))))
print("\n")

print(sorted(open("script2.py")))
print(list(zip(open("script2.py"), open("script2.py"))))
print(list(enumerate(open("script2.py"))))
print(list(filter(bool, open("script2.py"))))

import functools, operator

print(functools.reduce(operator.add, open("script2.py")))
print("\n")

print([line for line in open("script2.py")])
print("\n")

print(list(open("script2.py")))
print(tuple(open("script2.py")))
print("&&".join(open("script2.py")))
print("\n")

a, b, c, d, e = open("script2.py")
print(a, e)
a, *b = open("script2.py")
print(a, b)
print("y = 2\n" in open("script2.py"))
print("x = 2\n" in open("script2.py"))
L = [11, 22, 33, 44]
L[1:3] = open("script2.py")
print(L)
L = [11]
L.extend(open("script2.py"))
print(L)
print("\n")

L = [11]
L.append(open("script2.py"))
print(L)
print(list(L[1]))
print("\n")

print(set(open("script2.py")))
print({line for line in open("script2.py")})
print({ix: line for ix, line in enumerate(open("script2.py"))})
print("\n")

print({line for line in open("script2.py") if line[0] == "p"})
print({ix: line for ix, line in enumerate(open("script2.py")) if line[0] == "p"})
print("\n")

print(list(line.upper() for line in open("script2.py")))
print("\n")

print(sum([3, 2, 4, 1, 5, 0]))

print(any(["spam", "", "ni"]))
print(all(["spam", "", "ni"]))
print(max([3, 2, 5, 1, 4]))
print(min([3, 2, 5, 1, 4]))
print("\n")
