# 代码块分隔符：缩进规则
x = 1
if x:
    y = 2
    if y:
        print("block2")
    print("block1")
print("block0")
print("\n")

x = "SPAM"
if "rubbery" in "shrubbery":
    print(x * 8)
    x += "NI"
    if x.endswith("NI"):
        x *= 2
        print(x)
print("\n")


# 语句分隔符：行与行间连接符
L = ["Good", "Bad", "Ugly"]
print("\n")

a, b, c, d, e, f, g = 1, 1, 1, 1, 1, 1, 1
print(a, b, c, d, e, f)

if a == b and c == d and d == e and f == g:
    print("olde")

if a == b and c == d and d == e and e == f:
    print("new")
print("\n")

x = 1 + 2 + 3 + 4
print(x)
x = 1 + 2 + 3
+4
print(x)
print("\n")

x = 1
y = 2
print(x)
print("\n")

S = """
aaaa
bbbb
cccc"""
print(S)

S = "aaaa" "bbbb" "cccc"
print(S)
print("\n")

a, b = "hello", "world"
print(a, b)
print("hello" "world")
print("\n")

if 1:
    print("hello")
print("\n")


# 真值和布尔测试
print(2 < 3, 3 < 2)
print("\n")

print(2 or 3, 3 or 2)
print([] or 3)
print([] or {})
print({} or [])
print("\n")

print(2 and 3, 3 and 2)
print([] and {})
print(3 and [])
print("\n")


# if/else 三元表达式
X = 1
Y = 2
Z = 3
if X:
    A = Y
else:
    A = Z
print(A)
print("\n")

A = Y if X else Z

A = "t" if "spam" else "f"
print(A)
A = "t" if "" else "f"
print(A)
A = Y if X else Z
print("\n")

print(["f", "t"][bool("")])
print(["f", "t"][bool("spam")])
print("\n")

# filter函数调用和列表推导
L = [1, 0, 2, 0, "spam", "", "ham", []]
print(list(filter(bool, L)))
print([x for x in L if x])
print(any(L))
print(all(L))
# print(help(any))
# print(help(all(L)))
