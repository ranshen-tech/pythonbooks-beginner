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
