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


l = [1, 2, 3, "你好"]
print(len(l))
print(type(l))
stra = "我喜欢python"
print(len(stra))
print("\n")


l = [123, "ran", 3.14, True]
print(l)
print(l[0])
print(l[1:3])
print(l[2:])
print(l[::-1])
print(l * 2)
print("\n")


print("追加之前", l)
l.append(["fff", "ddd"])
l.append(8888)
print("追加之后", l)
l.insert(1, "这是我刚插入的数据")
print(l)
print("\n")


rsDate = list(range(10))
print(type(rsDate))
print(rsDate)
l.extend(rsDate)
print(l)
l.extend([3, 4, 5])
print(l)
print("\n")


li = [123, 3.14, "ranshen", True]
print("修改之前", li)
li[2] = 3232323
print("修改之后", li)
print("\n")


listB = list(range(10, 20))
print(listB)
del listB[0]
del listB[1:3]
listB.remove(14)
print(listB)
listB.pop(0)
print(listB)
print(listB.index(19))
print("\n")


tupleA = ()
tupleA = (123, "ranshen", 3.14, True)
print(type(tupleA))
