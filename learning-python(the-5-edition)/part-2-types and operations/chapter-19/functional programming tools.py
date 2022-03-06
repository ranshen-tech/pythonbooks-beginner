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

print(pow(3, 4))
print(list(map(pow, [1, 2, 3], [2, 3, 4])))
print("\n")

print(list(map(inc, [1, 2, 3, 4])))
print([inc(x) for x in [1, 2, 3, 4]])
print("\n")


# 选择可迭代对象中的元素：filter
print(list(range(-5, 5)))
print(list(filter(lambda x: x > 0, range(-5, 5))))
print("\n")

res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)

print(res)
print("\n")

print([x for x in range(-5, 5) if x > 0])
print("\n")


# 合并可迭代对象中的元素：reduce
from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4]))
print("\n")

L = [1, 2, 3, 4]
res = L[0]
for x in L[1:]:
    res += x

print(res)
print("\n")


def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally


print(myreduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(myreduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))
print("\n")

import operator, functools

print(functools.reduce(operator.add, [2, 4, 6]))
print(functools.reduce(lambda x, y: x + y, [2, 4, 6]))
