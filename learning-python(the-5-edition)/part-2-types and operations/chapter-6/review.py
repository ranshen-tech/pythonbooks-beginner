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
print("\n")

l1 = [2, 3, 4]
l2 = list(l1)
print(l2)
l1[0] = 24
print(l1)
print(l2)
print("\n")

l1 = [2, 3, 4]
l2 = l1.copy()
print(l1)
print(l2)
l1[0] = 24
print(l1)
print(l2)
print("\n")

s1 = set("spam")
print(s1)
s2 = s1.copy()
print(s2)
print("\n")

d1 = {"a": 1, "b": 2}
print(d1)
d2 = d1.copy()
print(d2)
d1["a"] = 3
print(d1)
print(d2)
print("\n")

s1 = set("spam")
print(s1)
s2 = set(s1)
print(s2)
print("\n")

d1 = {"a": 1, "b": 2}
print(d1)
d2 = dict(d1)
print(d2)
d1["a"] = 3
print(d1)
print(d2)
print("\n")


import copy

x = ["abc", 123]
y = copy.copy(x)
print(y)
x = ["abc", 123, {"a": 1, "b": 2}]
y = copy.copy(x)
print(x)

x = {"a": "abc", "b": [123], "c": [123]}
print(x)
y = copy.copy(x)
print(y)

y = copy.deepcopy(x)
print(y)
print("\n")
