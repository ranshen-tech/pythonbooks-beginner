# 在可迭代对象上映射函数：map


counters = [1, 2, 3, 4]

updated = []
for x in counters:
    updated.append(x + 10)

print(updated)
print("\n")


def inc(x):
    return x + 10


print(list(map(inc, counters)))
print("\n")

print(list(map(lambda x: x + 3, counters)))
print("\n")


def mymap(func, seq):
    res = []
    for x in seq:
        res.append(func(x))
    return res


print(list(map(inc, [1, 2, 3])))
print(mymap(inc, [1, 2, 3]))
print("\n")
