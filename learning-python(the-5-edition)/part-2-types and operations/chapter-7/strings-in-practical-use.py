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
