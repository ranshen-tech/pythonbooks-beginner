# 字符串
s = set("123")
print(s)
s = set("abc")
print(s)
print("\n")

print(len(str(2**1000)))
print("\n")

# print(s[len(s) - 1])
# 'set' object is not subscriptable

s = "shrubbery"
l = list(s)
print(l)
l[1] = "c"
print("".join(l))
print(",".join(l))
print("\n")

s = "spam"
print(s.isalpha())
print("\n")

line = "aaa, bbb, ccccc, dd\n"
print(line)
line = line.rstrip()
print(line)
print(line.split(", "))
print(line.rstrip().split(", "))
print("\n")

print("%.2f | %05d" % (3.14159, -42))
print("\n")

# 通用操作符都是以内置函数或表达式的形式出现；类型特定的操作是以方法调用的形式出现

print(s)
print(dir(s))
print("\n")

# __add__方法避免使用（速度慢）
print(s + "Ni!")
print(s.__add__("Ni!"))
print("\n")

# print(help(s.isalpha))
a = "bac3"
print(a.isalpha())
print("\n")

# print(help(s.replace))
print("spam".encode())
print("spam".encode("utf-8"))
print("spam".encode().decode())
print("\n")

print("x" + b"y".decode())
print("x".encode() + b"y")
print("\n")


# 列表
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])
print("\n")

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
g = [row for row in m]
print(type(g))
print(g)
print(sum([3, 4, 5]))
# print(help(sum))
# print(help(str.replace))
print("\n")

a = "bbbac"
print(a.replace("b", "r", 1))
print("\n")

# print(help(map))
# *解包元组项
somelist = list("spam")
parts = somelist[0], somelist[-1], somelist[1:3]
print(parts)
print(*parts)
print("\n")
