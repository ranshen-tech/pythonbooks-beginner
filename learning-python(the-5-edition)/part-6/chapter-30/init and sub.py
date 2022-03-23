# 构造函数表达式： __init__ and __sub__

from number import Number

X = Number(5)
Y = X - 2
print(Y.data)
print("\n")


# 索引和分片: __getitem__ and __setitem__


class Indexer:
    def __getitem__(self, index):
        return index**2


X = Indexer()
print(X[2])
print("\n")

for i in range(5):
    print(X[i], end=" ")
print("\n")


# 拦截分片


L = [5, 6, 7, 8, 9]
print(L[2:4])
print(L[1:])
print(L[:-1])
print(L[::2])
print("\n")

print(L[slice(2, 4)])
print(L[slice(1, None)])
print(L[slice(None, -1)])
print(L[slice(None, None, 2)])
print("\n")


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print("getitem:", index)
        return self.data[index]


X = Indexer()
print(X[0])
print(X[1])
print(X[-1])
print("\n")

print(X[2:4])
print(X[1:])
print(X[:-1])
print(X[::2])
print("\n")


class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print("indexing", index)
        else:
            print("slicing", index.start, index.stop, index.step)


X = Indexer()
X[99]
X[1:99:2]
X[1:]
print("\n")


# Python3中的__index__不是索引


class C:
    def __index__(self):
        return 255


X = C()
print(hex(X))
print(bin(X))
print(oct(X))
print("\n")

print(("C" * 256)[255])
print(("C" * 256)[X])
print(("C" * 256)[X:])
print("\n")


# 索引迭代: __getitem__


class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


X = StepperIndex()
X.data = "Spam"
print(X[1])

for item in X:
    print(item, end=" ")
print("\n")

print("p" in X)
print([c for c in X])
print(list(map(str.upper, X)))
a, b, c, d = X
print(a, c, d)
print(list(X), tuple(X), "".join(X))
print(X)
