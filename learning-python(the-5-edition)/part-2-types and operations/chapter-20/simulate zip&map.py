# Code example：用迭代工具simulate zip和map

S1 = "abc"
S2 = "xyz123"
print(list(zip(S1, S2)))
print("\n")

print(list(zip([-2, -1, 0, 1, 2, 3])))
print(list(zip([1, 2, 3], [2, 3, 4, 5])))
print("\n")

print(list(map(abs, [-2, -1, 0, 1, 2])))
print(list(map(pow, [1, 2, 3], [2, 3, 4, 5])))
print("\n")

print(list(map(lambda x, y: x + y, open("script2.py"), open("script2.py"))))
print([x + y for x, y in zip(open("script2.py"), open("script2.py"))])
print("\n")


# 编写自己的map(func, ...)
def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
print("\n")


def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]


print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))
print("\n")


def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        yield func(*args)


def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))
