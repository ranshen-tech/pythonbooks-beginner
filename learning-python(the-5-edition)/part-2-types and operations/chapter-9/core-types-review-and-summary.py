# class MySequence:
#     def __getitem__(self, index):
#         # Called on self[index], others
#     def __add__(self, other):
#         # Called on self + other
#     def __iter__(self):
#         # Preferred in iterations

X = [1, 2, 3]
print(X)
L = ["a", X, "b"]
D = {"x": X, "y": 2}

X[1] = "surprise"
print(L)
print(D)
print("\n")

L = [1, 2, 3]
D = {"a": 1, "b": 2}
A = L[:]
B = D.copy()

A[1] = "Ni"
B["c"] = "spam"
print(L, D)
print(A, B)
print("\n")

X = [1, 2, 3]
L = ["a", X[:], "b"]
D = {"x": X[:], "y": 2}
print(L, D)
print("\n")

import copy

Y = copy.deepcopy(X)
print(Y)
print("\n")


# 比较、等价性和真值
l1 = [1, ("a", 3)]
l2 = [1, ("a", 3)]
print(l1 == l2, l1 is l2)
print("\n")

s1 = "spam"
s2 = "spam"
print(s1 == s2, s1 is s2)
print("\n")

s1 = "a longer string1234567890"
s2 = "a longer string1234567890"
print(s1 == s2, s1 is s2)
print("\n")

l1 = [1, ("a", 3)]
l2 = [1, ("a", 2)]
print(l1 < l2, l1 == l2, l1 > l2)
print("\n")

print("b" < "c")
print("\n")

print(11 == "11")
a = ["-3", "22", "11"]
a.sort()
print(a)
print(str(11) >= "11", 11 >= int("11"))
print("\n")

d1 = {"a": 1, "b": 2}
d2 = {"a": 1, "b": 3}
print(d1 == d2)
# print(d1 < d2)
print("\n")

print(list(d1.items()))
print(sorted(d1.items()))
print(sorted(d1.items()) < sorted(d2.items()))
print("\n")


# Python中的True和False的含义
print(None)
if None != True:
    print(123)
print("\n")

l = [None] * 10
print(l)
print("\n")

print(bool(1))
print(bool("spam"))
print(bool(None))
print("\n")

print(type([1]) == type([]))
print(type([1]) == list())
print(list)
print(list())
print(isinstance([1], list))
print("\n")

import types


def f():
    pass


print(type(f) == types.FunctionType)
print(type(f))
print("\n")

l = [1, 2, 3]
m = ["x", l, "y"]
print(m)
l[1] = 0
print(m)
print("\n")

l = [1, 2, 3]
m = ["x", l[:], "y"]
l[1] = 0
print(l)
print(m)
print("\n")
