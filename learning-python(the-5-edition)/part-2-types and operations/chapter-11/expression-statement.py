x = print("spam")
print(x)
print("\n")


# 表达式语句和原位置修改
L = [1, 2]
L.append(3)
print(L)
print("\n")

L = L.append(4)
print(L)


# Python 3.X中print函数的应用
print()

x = "spam"
y = 99
z = ["eggs"]
print(x, y, z)
print("\n")


print(x, y, z, sep="")
print(x, y, z)
print(x, y, z, sep=", ")
print("\n")

print(x, y, z, end="")
print(x, y, z, end="")
print(x, y, z)
print(x, y, z, end="...\n")
print("\n")
