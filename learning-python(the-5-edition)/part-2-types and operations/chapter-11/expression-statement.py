x = print("spam")
print(x)
print("\n")


# 表达式语句和原位置修改
L = [1, 2]
L.append(3)
print(L)
print("\n")

L = L.append(4)
print(L)


# Python 3.X中print函数的应用
print()

x = "spam"
y = 99
z = ["eggs"]
print(x, y, z)
print("\n")


print(x, y, z, sep="")
print(x, y, z)
print(x, y, z, sep=", ")
print("\n")

print(x, y, z, end="")
print(x, y, z, end="")
print(x, y, z)
print(x, y, z, end="...\n")
print("\n")

print(x, y, z, sep="...", end="!\n")
print(x, y, z, end="!\n", sep="...")
print("\n")

print(x, y, z, sep="...", file=open("data.txt", "w"))
print(x, y, z)
print(open("data.txt").read())
print("\n")

text = "%s: %-.4f, %05d" % ("Result", 3.14159, 42)
print(text)
print("%s: %-.4f, %05d" % ("Result", 3.14159, 42))
print("\n")


# 打印流重定向
print("hello world")
print("\n")

import sys

sys.stdout.write("hello world\n")
print("\n")


# 手动定向输出流
x = 1
y = 2
z = 3
print(x, y)

import sys

temp = sys.stdout
sys.stdout.write(str(x) + " " + str(y) + "\n")
print("\n")

sys.stdout = open("log.txt", "a")
print(x, y, x)


# 自动流重定向
print("spam")
print(1, 2, 3)
sys.stdout.close()
sys.stdout = temp

print("back here")
print(open("log.txt").read())
print("\n")

a = 4
b = 5
c = 6
log = open("log.txt", "a")
print(x, y, z, file=log)
print(a, b, c)
print("\n")

log = open("log.txt", "w")
print(1, 2, 3, file=log)
print(4, 5, 6, file=log)
log.close()
print(7, 8, 9)
print(open("log.txt").read())
print("\n")

sys.stderr.write(("Bad!" * 8) + "\n")
print("Bad!" * 8, file=sys.stderr)
print("Bad!" * 8)
print("\n")

X = 1
Y = 2
print(X, Y)
sys.stdout.write(str(X) + " " + str(Y) + "\n")

print(X, Y, file=open("temp1", "w"))
open("temp2", "w").write(str(X) + " " + str(Y) + "\n")

print(open("temp1", "rb").read())
print(open("temp2", "rb").read())
print("\n")

print("spam")
print("spam", "ham", "eggs")
print()
print("")
print("\n")

print("%s %s %s" % ("spam", "ham", "eggs"))
print("{0} {1} {2}".format("spam", "ham", "eggs"))
print("answer " + str(42))
print("\n")
