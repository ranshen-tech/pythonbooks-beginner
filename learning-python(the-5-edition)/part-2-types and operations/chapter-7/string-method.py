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
