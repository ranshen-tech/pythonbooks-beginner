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
