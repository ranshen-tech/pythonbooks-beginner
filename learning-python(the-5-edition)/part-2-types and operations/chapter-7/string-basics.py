S = r"\temp\spam"
print(S)

print("s\tp\na\0m")
print("\n")


# 单引号和双引号字符串是一样的
print("shrubbery", "shrubbery")
print('knight"s', "knight's")
print("\n")

title = "Meaning " "of" " Life"
print(title)
print("Meaning " "of" " Life")
print("knight's", 'knight"s')
print("\n")


# 转义序列代表特殊字符
s = "a\nb\tc"
print(s)
print(len(s))
print("\n")

print("------------------")
print("h\na\vp\vp\vy")
print("r\va\vn\vs\vh\ve\vn\n")

s = "a\0b\0c"
print(s)
print(len(s))
print("\n")

s = "\001\002\x03"
print(s)
print(len(s))
print("\n")

S = "s\tp\na\x00m"
print(S)
print(len(S))
