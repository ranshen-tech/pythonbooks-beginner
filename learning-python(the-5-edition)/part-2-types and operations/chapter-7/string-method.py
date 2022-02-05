# 方法调用语法
S = "spam"
result = S.find("pa")
print(result)
print("\n")

# 修改字符串 ||
S = "spammy"
S = S[:3] + "xx" + S[5:]
print(S)
print("\n")

S = "spammy"
S = S.replace("mm", "xx")
print(S)
print("\n")

print("aa$bb$cc$dd".replace("$", "SPAM"))
print("\n")

S = "xxxxSPAMxxxxSPAMxxxx"
where = S.find("SPAM")
print(where)
S = S[:where] + "EGGS" + S[(where + 4) :]
print(S)
print("\n")

S = "xxxxSPAMxxxxSPAMxxxx"
print(S.replace("SPAM", "EGGS"))
print(S)
print(S.replace("SPAM", "EGGS", 1))
print("\n")

S = "spammy"
L = list(S)
print(L)
print("\n")

L[3] = "x"
L[4] = "x"
print(L)

S = "".join(L)
print(S)

print("SPAM".join(["eggs", "sausage", "ham", "toast"]))
print("\n")


# 字符串方法示例：解析文本
line = "aaa bbb ccc"
col1 = line[0:3]
col3 = line[8:]
print(col1)
print(col3)
print("\n")

line = "aaa bbb ccc"
cols = line.split()
print(cols)
print("\n")

line = "bob,hacker,40"
print(line.split(","))

line = "i'mSPAMaSPAMlumberjack"
print(line.split("SPAM"))
print("\n")


# 实际应用中的其他常见字符串方法
line = "The knights who say Ni!\n"
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith("Ni!\n"))
print(line.startswith("The"))
print("\n")

print(line)

print(line.find("Ni") != -1)
print("Ni" in line)

sub = "Ni!\n"
print(line.endswith(sub))

print(line[-len(sub) :] == sub)
print("\n")

S = ""
# print(help(S.upper))


# 原始 string 模块的函数（在Python3中删除）
S = "a+b+c+"
x = S.replace("+", "spam")
print(x)

# import string

# y = string.replace(S, "+", "spam")
# print(y)
