# list comprehension VS map

print(ord("s"))
print(chr(115))
print("\n")

res = []
for x in "spam":
    res.append(ord(x))

print(res)
print("\n")

res = list(map(ord, "spam"))
print(res)
print("\n")

res = [ord(x) for x in "spam"]
print(res)
print("\n")

print([x**2 for x in range(10)])
print("\n")

print(list(map(lambda x: x**2, range(10))))
print("\n")

# 使用filter增加测试和循环嵌套

print([x for x in range(5) if x % 2 == 0])

print(list(filter(lambda x: x % 2 == 0, range(5))))

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)

print(res)
print("\n")

print([x**2 for x in range(10) if x % 2 == 0])

print(list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(10)))))
print("\n")


# standard comprehension grammar

# [expression for target in iterable]

# [expression for target1 in iterable1 if condition1
#             for target2 in iterable2 if condition2 ...
#             for targetN in iterableN if conditionN]

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)

res = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)

print(res)
print("\n")
