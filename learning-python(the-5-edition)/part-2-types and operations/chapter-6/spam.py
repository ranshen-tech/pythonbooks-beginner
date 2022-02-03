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


# 共享引用和在原位置修改
L1 = [2, 3, 4]
print(L1)
L2 = L1
print(L2)
L1 = 24
print(L1)
print(L2)
print("\n")

L1 = [2, 3, 4]
L2 = L1
L1[0] = 24

print(L1)
print(L2)
print("\n")

L1 = [2, 3, 4]
# L2 = L1[:]
# L2 = list(L1)
L2 = L1.copy()
print(L2)
L1[0] = 24

print(L1)
print(L2)
print("\n")

import copy

Y = {"a": 1, "b": 2, "c": [3, 4, 5]}
X = copy.copy(Y)
print(X)
X = copy.deepcopy(Y)
print(X)
print("\n")

# 共享引用和相等
x = 42
x = "shrubbery"


L = [1, 2, 3]
M = L
print(L == M)
print(L is M)
print("\n")

L = [1, 2, 3]
M = [1, 2, 3]
print(L == M)
print(L is M)
print("\n")

X = 42
Y = 42
print(X == Y)
print(X is Y)
print("\n")

import sys

print(sys.getrefcount(1))
print("\n")

# exercise
A = "spam"
B = A
B = B + "shrubbery"

print(A)
print(B)
print("\n")

A = ["spam"]
B = A
B[0] = "shrubbery"
print(A)
print(B)
print("\n")

A = ["spam"]
B = A[:]
B[0] = "shrubbery"
print(B)
print(A)
