# 基本列表操作
print(len([1, 2, 3]))
print([1, 2, 3] + [4, 5, 6])
print(["Ni!"] * 4)
print("\n")

print(str([1, 2]) + "34")
print([1, 2] + list("34"))
print("\n")


# 列表迭代和推导
print(3 in [1, 2, 3])
for x in [1, 2, 3]:
    print(x, end=" ")
print("\n")

res = [c * 4 for c in "SPAM"]
print(res)
print("\n")

res = []
for c in "SPAM":
    res.append(c * 4)
print(res)
print("\n")

print(list(map(abs, [-1, -2, 0, 1, 2])))
print("\n")

# 索引、分片和矩阵
L = ["spma", "Spam", "SPAM!"]
print(L[2])
print(L[-2])
print(L[1:])
print("\n")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
print(matrix[1][1])
print(matrix[2][0])
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])
print("\n")


# 索引与分片的赋值
L = ["spam", "Spam", "SPAM!"]
L[1] = "eggs"
print(L)

L[0:2] = ["eat", "more"]
print(L)
print("\n")

L = [1, 2, 3]
L[1:2] = [4, 5]
print(L)
L[1:1] = [6, 7]
print(L)
L[2:5] = L[3:6]
print(L)
L[1:2] = []
print(L)
print("\n")

L = [1]
L[:0] = [2, 3, 4]
print(L)
L[len(L) :] = [5, 6, 7]
print(L)
L.extend([8, 9, 10])
print(L)
print("\n")


# 列表方法调用
L = ["eat", "more", "SPAM!"]
L.append("please")
print(L)
L.sort()
print(L)
print("\n")


# 更多的关于列表排序
L = ["abc", "ABD", "aBe"]
L.sort()
print(L)
L = ["abc", "ABD", "aBe"]
L.sort(key=str.lower)
print(L)
L = ["abc", "ABD", "aBe"]
L.sort(key=str.lower, reverse=True)
print(L)
print("\n")

L = ["abc", "ABD", "aBe"]
print(sorted(L, key=str.lower, reverse=True))
L = ["abc", "ABD", "aBe"]
print(sorted([x.lower() for x in L], reverse=True))
print("\n")


# 其他常见的列表方法
