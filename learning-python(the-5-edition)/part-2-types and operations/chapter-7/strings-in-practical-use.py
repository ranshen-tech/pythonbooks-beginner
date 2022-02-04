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
