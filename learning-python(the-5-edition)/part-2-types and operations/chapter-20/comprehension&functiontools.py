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
