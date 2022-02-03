# 类型属于对象，而不是变量
a = 3
print([1, a])
a = "spam"
print(a)
print([1, a])
a = 1.23
print("\n")


# 对象的垃圾回收
x = 42
x = "shrubbery"
x = 3.1415
x = [1, 2, 3]

x.append(x)
print(x)
print(len(x))
print("\n")


# 共享引用
a = 3
b = a
print(b)
a = "spam"
print(a)
print(b)
print("\n")

a = 3
print(a)
b = a
print(b)
a = a + 2
print(a)
print("\n")
