test = "python"
print(f"获取第一个字符:{test[0]}")
print(f"获取第一个字符:{test[1]}")
for item in test:
    print(item, end=" ")
print("\n")


name = "ranshen"
print(f"姓名首字母转换大写: {name.capitalize()}")
print("\n")


name = "   ran shen   "
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print("\n")


b = name
print(b)
# id函数可以查看一个对象的内存地址
print(f"name的内存地址{id(name)}")
print(f"b的内存地址{id(b)}")
print("\n")


dateStr = "i love Python"
# find可以查找目标对象在序列对象中的位置
print(dateStr.find("p"))
print(dateStr.index("o"))
print("\n")


print(dateStr.startswith("i"))
print(dateStr.startswith("io"))
print(dateStr.endswith("o"))
print(dateStr.endswith("n"))
print(dateStr.endswith("on"))
print("\n")


print(dateStr.lower())
print(dateStr.upper())
print("\n")


msg = "hello world"
print(msg[0])
print(msg[2:5])
print(msg[2:])
print(msg[:3])
print(msg[::-1])
print("\n")
