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
print("\n")

x = "C:\py\code"
print(x)
print(len(x))
print("\n")


# 原始字符串阻止转义
print("C:\new\text.dat")
print(r"C:\new\text.dat")
print("C:\\new\\text.dat")
print("\n")

path = r"C:\new\text.dat"
print(path)
print(len(path))
print("C:/new/text.dat")
print("\n")

print(r"...\\")
print(r"1\nb\tc\\"[:-1])
print(r"1\nb\tc" + "\\")
print("1\\nb\\tc\\")
print("\n")


# 三引号编写多行块字符串
mantra = """Always look
 on the bright
side of life."""

print(mantra)
print("\n")

menu = """spam   # comments here added to string!
eggs             # ditto
"""
print(menu)

menu = "spam\n" "eggs\n"  # comments here ignored  # but newlines not automatic
print(menu)
print("\n")

X = 1
"""
import os
print(os.getcwd())
"""
Y = 2
