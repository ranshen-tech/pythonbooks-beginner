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

S1 = {1, 2, 3, 4}
print(S1 & {1, 3})
print({1, 5, 3, 6} | S1)
print(S1 - {1, 3, 4})
print(S1 > {1, 3})
print("\n")

print(S1 - {1, 2, 3, 4})
print(type({}))

S = set()
S.add(1.23)
print(S)
print("\n")

print({1, 2, 3} | {3, 4})
# print({1, 2, 3} | [3, 4])
print({1, 2, 3}.union([3, 4]))
print({1, 2, 3}.union({3, 4}))
print({1, 2, 3}.union(set([3, 4])))
print({1, 2, 3}.intersection((1, 3, 5)))
print({1, 2, 3}.issubset(range(-5, 5)))
print("\n")

# 不可变性限制与冻结集合
print(S)
# S.add([1, 2, 3])
# S.add({"a": 1})
S.add((1, 2, 3))
print(S)
print("\n")

print(S | {(4, 5, 6), (1, 2, 3)})
print((1, 2, 3) in S)
print((1, 4, 3) in S)
print("\n")


# Python3.X 和 2.7中的集合推导
print({x**2 for x in [1, 2, 3, 4]})
print({x for x in "spma"})
print("\n")

print({c * 4 for c in "spma"})
print({c * 4 for c in "spamham"})
print("\n")

S = {c * 4 for c in "spma"}
print(S | {"mmmm", "xxxx"})
print(S & {"mmmm", "xxxx"})
print("\n")

# 为什么使用集合
L = [1, 2, 1, 3, 2, 4, 5]
print(set(L))
L = list(set(L))
print(L)
print("\n")

print(list(set(["yy", "cc", "aa", "xx", "dd", "aa"])))
print("\n")

print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))
print(set("abcdefg") - set("abdghij"))
print(set("spma") - set(["h", "a", "m"]))
print("\n")

print(set(dir(bytes)) - set(dir(bytearray)))
print(set(dir(bytearray)) - set(dir(bytes)))
print("\n")

L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2)
print(set(L1) == set(L2))
print(sorted(L1) == sorted(L2))
print("spma" == "asmp", set("spam") == set("asmp"), sorted("spam") == sorted("asmp"))
print("\n")

engineers = {"bob", "sue", "ann", "vic"}
managers = {"tom", "sue"}

print("bob" in engineers)
print(engineers & managers)

print(engineers | managers)
print(engineers - managers)

print(managers - engineers)

print(engineers > managers)
print({"bob", "sue"} < engineers)

print((managers | engineers) > managers)

print(managers ^ engineers)

print((managers | engineers) - (managers ^ engineers))
print("\n")

# 布尔型
print(type(True))
print(isinstance(True, int))
print(True == 1)
print(True is 1)
print(True or False)
print(True + 4)
