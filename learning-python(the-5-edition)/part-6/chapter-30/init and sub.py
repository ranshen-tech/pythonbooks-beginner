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
