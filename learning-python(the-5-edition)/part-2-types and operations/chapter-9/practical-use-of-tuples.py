t = tuple("spam")
print(t)
print(len(t))
print(t * 3)
print("\n")

print((1, 2) + (3, 4))
print((1, 2) * 4)
t = (1, 2, 3, 4)
print(t[0])
print(t[1:3])
print(t[0], t[1:3])
print("\n")

x = 40
print(x)
print(type(x))
y = (40,)
print(y)
print(type(y))
print("\n")


# 转换、方法和不可变性
t = ("cc", "aa", "dd", "bb")
tmp = list(t)
tmp.sort()
print(tmp)
print(t)
t = tuple(tmp)
print(t)
print("\n")

t = ("cc", "aa", "dd", "bb")
print(t)
sorted(t)
print(t)
print(sorted(t))
print("\n")

s = "acb"
s1 = list(s)
s1.sort()
print(s1)
s2 = "".join(s1)
print(s2)
print("\n")

s = "acb"
print(sorted(s))
print(s)
