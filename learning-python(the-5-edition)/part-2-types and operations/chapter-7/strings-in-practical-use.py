# 基本操作
print(len("abc"))
print(("abc" + "def"))
print("Ni!" * 4)
print("-" * 80)
print("\n")

myjob = "hacker"
for c in myjob:
    print(c, end=" ")
print()
print("k" in myjob)
print("z" in myjob)
print("spam" in "abcspamdef")
print("\n")


# 索引和分片
S = "spam"
print(S[0], S[-2])
print(S[1:3], S[1:], S[:-1])
print("\n")


# 扩展分片：第三个限制值和分片对象
S = "abcdefghijklmnop"
print(S[1:10:2])
print(S[::2])
print("\n")

S = "hello"
print(S[::-1])
print("\n")

S = "abcdefg"
print(S[5:1:-1])
print("\n")

print("spam"[1:3])
print("spam"[slice(1, 3)])
print("spam"[::-1])
print("spam"[slice(None, None, -1)])
print("\n")


# 字符串转换工具
# print("42" + 1)
print(int("42"), str(42))
print(repr(42))
print(len(repr(42)))
print(type(repr(42)))
print("\n")

print(str("spam"), repr("spam"))
print("\n")

S = "42"
I = 1
print(int(S) + I)

print(S + str(I))
print("\n")

print(str(3.1415), float("1.5"))

text = "1.234E-10"
print(float(text))
print("\n")


# 字符串代码转换
print(ord("s"))
print(chr(115))
print("\n")

S = "5"
S = chr(ord(S) + 1)
print(S)

S = chr(ord(S) + 1)
print(S)
print("\n")

print(int("5"))
print(ord("5") - ord("0"))
print(ord("5"))
print(ord("0"))
print("\n")

print(ord("1"))
I = 1
I = 3
I = 6
I = 13

B = "1101"
print(type(B[0]))
I = 0
while B != "":
    I = I * 2 + (ord(B[0]) - ord("0"))
    B = B[1:]

print(I)
print("\n")

print(int("1101", 2))
print(bin(13))
print("\n")


# 修改字符串｜
S = "spam"
S = S + "SPAM!"
print(S)
S = S[:4] + "Burger" + S[-1]
print(S)
print("\n")

S = "splot"
S = S.replace("pl", "pamal")
print(S)
print("\n")

msg = "That is %d %s bird!" % (1, "dead")
print(msg)
msg = "That is {0} {1} bird!".format(1, "dead")
print(msg)
