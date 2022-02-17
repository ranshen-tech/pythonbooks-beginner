# Numbers
print(2**16)
print(2 / 5, 2 / 5.0)
print("\n")


# String
print("spam" + "eggs")
s = "ham"
print("eggs" + s)
print(s * 5)
print(s[:0])

print("green %s and %s" % ("eggs", s))
print("green {0} and {1}".format("eggs", s))
print("\n")


# Tuples
print(("x",)[0])
print(("x", "y")[1])
print("\n")


# Lists
L = [1, 2, 3] + [4, 5, 6]
print(L, L[:], L[:0], L[-2], L[-2:])
print(([1, 2, 3] + [4, 5, 6])[2:4])
print([L[2], L[3]])
L.reverse()
print(L)
L.sort()
print(L)
print(L.index(4))
print("\n")


# Dictionaries
print({"a": 1, "b": 2}["b"])
D = {"x": 1, "y": 2, "z": 3}
D["w"] = 0
print(D["x"] + D["w"])
D[(1, 2, 3)] = 4
print(D)
print(list(D.keys()), list(D.values()), (1, 2, 3) in D)
print("\n")


# Empties
print([[]], "", [], (), {}, None)
print("\n")


# 索引运算和分片运算
L = [1, 2, 3, 4]
print(L[-1000:100])
print(L[3:1])
print(L)
L[3:1] = ["?"]
print(L)
print("\n")


# 索引运算、分片运算以及del
L = [1, 2, 3, 4]
L[2] = []
print(L)
L[2:3] = []
print(L)
del L[0]
print(L)
del L[1:]
print(L)
# L[1:2] = 1
# print(L)
print("\n")


# 元组赋值运算
X = "spam"
Y = "eggs"
X, Y = Y, X
print(X)
print(Y)
print("\n")


# 字典键
D = {}
D[1] = "a"
D[2] = "b"
D[(1, 2, 3)] = "c"
print(D)
print("\n")


# 字典索引运算
D = {"a": 1, "b": 2, "c": 3}
print(D["a"])
# print(D["d"])
D["d"] = 4
print(D)
L = [0, 1]
# print(L[2])
# L[2] = 3
print(L)
print("\n")


# 通用操作。习题解答
# print("x" + 1)
# print({} + {})
l = []
l.append(9)
print(l)
s = ""
# s.append(9)
print(list({}.keys()))
# print([].keys())
print([][:])
print(""[:])


# 字符串索引运算
S = "spam"
print(S[0][0][0][0][0])
