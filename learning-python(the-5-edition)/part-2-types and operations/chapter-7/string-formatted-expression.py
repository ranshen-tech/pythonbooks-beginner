# 格式化表达式基础
print("That is %d %s bird" % (1, "dead"))
print("\n")

exclamation = "Ni"
print("The knights who say %s!" % exclamation)

print("%d %s %g you" % (1, "spam", 4.0))

print("%s -- %s -- %s" % (42, 3.14159, [1, 2, 3]))
print("\n")


# 高级格式化表达式举例
x = 1234
res = "integers: ...%d...%-6d...%06d" % (x, x, x)
print(res)
print("\n")

x = 1.23456789
print(x)

print("%e | %f | %g" % (x, x, x))

print("%E" % x)
print("\n")

print("%-6.2f | %05.2f | %+06.1f" % (x, x, x))

print("%s" % x, str(x))
print("\n")

print("%f, %.2f, %.*f" % (1 / 3.0, 1 / 3.0, 4, 1 / 3.0))
print("\n")


# 基于字典的格式化表达式
print("%(qty)d more %(food)s" % {"qty": 1, "food": "spam"})
print("\n")

reply = "Greetings...\nHello %(name)s!\nYour age is %(age)s"

values = {"name": "Bob", "age": 40}
print(reply % values)
print("\n")

food = "spam"
qty = 10
print(vars())
print("\n")

print("%(qty)d more %(food)s" % vars())
