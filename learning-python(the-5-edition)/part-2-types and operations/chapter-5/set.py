# Python 2.6 及之前版本中的集合基础知识
x = set("abcde")
y = set("bdxyz")

print(x)
print(x - y)
print(x | y)
print(x & y)
print(x ^ y)
print(x > y, x < y)
print("\n")

print("e" in x)
print("e" in "Camelot", 22 in [11, 22, 33])
print("\n")

z = x.intersection(y)
print(z)
z.add("spam")
print(z)
z.update("X", "Y")
print(z)
z.remove("b")
print(z)
print("\n")

for item in set("abc"):
    print(item * 3)
print("\n")

S = set([1, 2, 3])
print(S)
print(S | set([3, 4]))
print(type(S | set([3, 4])))
# print(S | [3, 4])
print(S.union([3, 4]))
print(S.intersection([1, 3, 5]))
print(S.issubset(range(-5, 5)))
print("\n")


# Python3.X 和 Python2.7中的集合字面量
print(set([1, 2, 3, 4]))
print({1, 2, 3, 4})
print("\n")

print(set([1, 2, 3, 4]))
print(set("spam"))
print({1, 2, 3, 4})
S = {"s", "p", "a", "m"}
print(S)

S.add("alot")
print(S)
print("\n")
