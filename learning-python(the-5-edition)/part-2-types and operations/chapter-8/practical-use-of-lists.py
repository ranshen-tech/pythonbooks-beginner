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


# 原位置修改列表
