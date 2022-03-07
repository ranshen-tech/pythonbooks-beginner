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
print("\n")

res = []
for x in [0, 1, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)

print(res)
print("\n")

print([x + y for x in "spam" for y in "SPAM"])
print("\n")

print([x + y for x in "spam" if x in "sm" for y in "SPAM" if y in ("P", "A")])
print("\n")

print(
    [
        x + y + z
        for x in "spam"
        if x in "sm"
        for y in "SPAM"
        if y in ("P", "A")
        for z in "123"
        if z > "1"
    ]
)
print("\n")

print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
print("\n")

res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))
print(res)
print("\n")


# example: comprehension & 矩阵

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]

print(M[1])
print(M[1][2])
print("\n")

print([row[1] for row in M])
print([M[row][1] for row in (0, 1, 2)])
print("\n")

print([M[i][i] for i in range(len(M))])
print([M[i][len(M) - 1 - i] for i in range(len(M))])
print("\n")

L = [[1, 2, 3], [4, 5, 6]]
for i in range(len(L)):
    for j in range(len(L[i])):
        L[i][j] += 10
print(L)
print("\n")

print([col + 10 for row in M for col in row])
print([[col + 10 for col in row] for row in M])
print("\n")

res = []
for row in M:
    for col in row:
        res.append(col + 10)
print(res)

res = []
for row in M:
    tmp = []
    for col in row:
        tmp.append(col + 10)
    res.append(tmp)

print(res)
print("\n")

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]

print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])
print([[M[row][col] * N[row][col] for col in range(3)] for row in range(3)])
print("\n")

res = []
for row in range(3):
    tmp = []
    for col in range(3):
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)

print(res)
print("\n")

print([[col1 * col2 for col1, col2 in zip(row1, row2)] for row1, row2 in zip(M, N)])

res = []
for row1, row2 in zip(M, N):
    tmp = []
    for col1, col2 in zip(row1, row2):
        tmp.append(col1 * col2)
    res.append(tmp)
print(res)
