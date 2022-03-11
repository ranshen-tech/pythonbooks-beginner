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


print(list(mymap(abs, [-2, -1, 0, 1, 2])))
print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))
print("\n")


# 编写自己的zip(...)和map(None, ...)

print(map(None, [1, 2, 3], [2, 3, 4, 5]))
print(map(None, "abc", "xyz123"))
print("\n")


def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    # print(seqs)
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res


S1, S2 = "abc", "xyz123"
print(myzip(S1, S2))
print("\n")

print(mymapPad(S1, S2))
print(mymapPad(S1, S2, pad=99))
print("\n")


def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)


def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)


S1, S2 = "abc", "xyz123"
print(list(myzip(S1, S2)))
print(list(mymapPad(S1, S2)))
print(list(mymapPad(S1, S2, pad=99)))
print("\n")


def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]


S1, S2 = "abc", "xyz123"
print(myzip(S1, S2))


def mymapPad(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]


print(mymapPad(S1, S2))
print(mymapPad(S1, S2, pad=99))
