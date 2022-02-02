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
z.update()
