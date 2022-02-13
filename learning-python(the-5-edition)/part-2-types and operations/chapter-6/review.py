# 共享引用
a = 3
print(a)
b = a
print(b)
print("\n")

a = 3
b = a
a = "spam"
print(a)
print(b)
print("\n")

a = 3
b = a
b = "spam"
print(b)
print(a)
print("\n")

l1 = [2, 3, 4]
l2 = l1
l1[0] = 24
print(l1)
print(l2)
print("\n")

l1 = [2, 3, 4]
l2 = l1[:]
l1[0] = 24
print(l1)
print(l2)
