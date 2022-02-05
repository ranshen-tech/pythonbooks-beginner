# 字符串格式化方法基础
template = "{0}, {1} and {2}"
print(template.format("spam", "ham", "eggs"))
print(template, "\n")

template = "{motto}, {pork} and {food}"
print(template.format(motto="spam", pork="ham", food="eggs"))

template = "{motto}, {0} and {food}"
print(template.format("ham", motto="spam", food="eggs"))

template = "{}, {} and {}"
print(template.format("spam", "ham", "eggs"))
print("\n")

template = "%s, %s and %s"
print(template % ("spam", "ham", "eggs"))

template = "%(motto)s, %(pork)s and %(food)s"
print(template % dict(motto="spam", pork="ham", food="eggs"))
print("\n")

print("{motto}, {0} and {food}".format(42, motto=3.14, food=[1, 2]))
print("\n")

X = "{motto}, {0} and {food}".format(42, motto=3.14, food=[1, 2])
print(X)

print(X.split(" and "))

Y = X.replace("and", "but under no circumstances")
print(Y)
print("\n")


# 添加键、属性和偏移量
import sys

print("My {1[kind]} runs {0.platform}".format(sys, {"kind": "laptop"}))

print("My {map[kind]} runs {sys.platform}".format(sys=sys, map={"kind": "laptop"}))
print("\n")

somelist = list("SPAM")
print(somelist)

print("first={0[0]}, third={0[2]}".format(somelist))

print("first={0}, third={1}".format(somelist[0], somelist[-1]))
print("\n")

parts = somelist[0], somelist[-1], somelist[1:3]
print(parts)
print(type(parts))
print("first={0}, last={1}, middle={2}".format(*parts))
print(*parts)
print("\n")

# 高级格式化方法举例
print("{0:10} = {1:10}".format("spam", 123.4567))
print(12345678910012345678910)
print("\n")

print("{0:>10} = {1:<10}".format("spam", 123.4567))
print("{0.platform:>10} = {1[kind]:<}".format(sys, dict(kind="laptop")))
print("\n")

print("{:10} = {:10}".format("spam", 123.4567))
print("{:>10} = {:<10}".format("spam", 123.4567))
print("{.platform:>10} = {[kind]:<10}".format(sys, dict(kind="laptop")))
print("\n")

print("{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159))
print("{0:f}, {1:.2f}, {2:06.2f}".format(3.14159, 3.14159, 3.14159))
print("\n")

print("{0:X}, {1:o}, {2:b}".format(255, 255, 255))
print(bin(255), int("11111111", 2), 0b11111111)
print(hex(255), int("FF", 16), 0xFF)
print(oct(255), int("377", 8), 0o377)
print("\n")

print("{0:.2f}".format(1 / 3.0))
print("%.2f" % (1 / 3.0))
print("\n")

print("{0:.{1}f}".format(1 / 3.0, 4))
print("%.*f" % (4, 1 / 3.0))
print("\n")

print("{0:.2f}".format(1.2345))
print(format(1.2345, ".2f"))
print("%.2f" % 1.2345)


# 与%格式化表达式比较
