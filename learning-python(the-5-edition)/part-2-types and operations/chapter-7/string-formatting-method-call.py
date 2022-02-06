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
print("\n")

# 与%格式化表达式比较
print("%s=%s" % ("spam", 42))
print("{0}={1}".format("spam", 42))
print("{}={}".format("spam", 42))
print("\n")

print("%s, %s and %s" % (3.14, 42, [1, 2]))
print("My %(kind)s runs %(platform)s" % {"kind": "laptop", "platform": sys.platform})
print("My %(kind)s runs %(platform)s" % dict(kind="laptop", platform=sys.platform))

somelist = list("SPAM")
parts = somelist[0], somelist[-1], somelist[1:3]
print(type(parts))
print("first=%s, last=%s, middle=%s" % parts)
print("\n")

print("%-10s = %10s" % ("spam", 123.4567))
print("%10s = %-10s" % ("spam", 123.4567))
print("%(plat)10s = %(kind)-10s" % dict(plat=sys.platform, kind="laptop"))
print("\n")

print("%e, %.3e, %g" % (3.14159, 3.14159, 3.14159))
print("%f, %.2f, %06.2f" % (3.14159, 3.14159, 3.14159))
print("%x, %o" % (255, 255))
print("\n")

import sys

print("My {1[kind]:<8} runs {0.platform:>8}".format(sys, {"kind": "laptop"}))
print("My %(kind)-8s runs %(plat)8s" % dict(kind="laptop", plat=sys.platform))
print("\n")

data = dict(platform=sys.platform, kind="laptop")
print(data)
print("My {kind:<8} runs {platform:>8}".format(**data))
print("My %(kind)-8s runs %(platform)8s" % data)
print("\n")

print("{0:d}".format(999999999999))
print("{0:,d}".format(999999999999))
print("\n")

print("{:,d}".format(999999999999))
print("{:,d} {:,d}".format(999999999, 8888888))
print("{:,.2f}".format(296999.2567))
print("\n")


# 为什么使用格式化方法
print("{0:b}".format((2**16) - 1))
# print("%b" % ((2**16) - 1))

print(bin((2**16) - 1))
print("%s" % bin((2**16) - 1))
print("{}".format(bin((2**16) - 1)))

print("%s" % bin((2**16) - 1)[2:])
print("\n")

print("{:,d}".format(999999999999))
print("\n")


# 灵活的引用语法：额外的发杂性和功能的重叠
print("{name} {job} {name}".format(name="Bob", job="dev"))
print("%(name)s %(job)s %(name)s" % dict(name="Bob", job="dev"))
print("\n")

D = dict(name="Bob", job="dev")
print("{0[name]} {0[job]} {0[name]}".format(D))
print("{name} {job} {name}".format(**D))
print("%(name)s %(job)s %(name)s" % D)
print("\n")


# 显式的值的引用：如今变得可选和不常用
# print("\n%s<Class %s, address %s:\n%s%s%s>\n" % (...))
# print("\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n".format(...))

print("The {0} side {1} {2}".format("bright", "of", "life"))
print("The {} side {} {}".format("bright", "of", "life"))
print("The %s side %s %s" % ("bright", "of", "life"))
print("\n")

print("{0:f}, {1:.2f}, {2:05.2f}".format(3.14159, 3.14159, 3.14159))
print("{:f}, {:.2f}, {:06.2f}".format(3.14159, 3.14159, 3.14159))
print("%f, %.2f, %06.2f" % (3.14159, 3.14159, 3.14159))
print("\n")


# 命名的方法与上下文中立的参数：美学 vs 实用
print("%.2f" % 1.2345)
print("%.2f %s" % (1.2345, 99))
print("\n")

print("%s" % 1.23)
print("%s" % (1.23,))
print("%s" % ((1.23,),))
print("\n")

print("{0:.2f}".format(1.2345))
print("{0:.2f} {1}".format(1.2345, 99))
print("{0}".format(1.23))
print("{0}".format((1.23,)))
print("\n")

print(type((1.23)))
print(type((1.23,)))
print("\n")


# 功能 vs 表达式：微小的便利
def myformat(fmt, args):
    return fmt % args


print(myformat("%s %s", (88, 99)))
print(str.format("{} {}", 88, 99))
print(format(3.1415, ".2f"))
print("\n")

print("%(num)i = %(title)s" % dict(num=7, title="Strings"))
print("{num:d} = {title:s}".format(num=7, title="Strings"))
print("{num} = {title}".format(**dict(num=7, title="Strings")))
print("\n")

import string

t = string.Template("$num = $title")
print(t.substitute({"num": 7, "title": "Strings"}))
print(t.substitute(num=7, title="Strings"))
print(t.substitute(dict(num=7, title="Strings")))
print("\n")

print("%d = %s" % (7, "Strings"))
print("{} = {}".format(7, "Strings"))
