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
tupleA = (123, "ranshen", 3.14, True, [11, 22, 33])
print(type(tupleA))
print(tupleA)
for item in tupleA:
    print(item, end=" ")
print("\n")


print(tupleA[2:4])
print(tupleA[::-1])
print(tupleA[::-2])
print(tupleA[::-3])
print(tupleA[-2:-1:])
print("\n")


tupleA[4][0] = 519
print(tupleA)
print("\n")


tupleB = 1
print(type(tupleB))
tupleB = "1"
print(type(tupleB))
tupleB = (1,)
print(type(tupleB))
print(tupleB)
print("\n")


tupleC = range(10)
print(type(tupleC))
tupleC = tuple(range(10))
print(type(tupleC))
print(tupleC)
print(tupleC.count(7))
tupleC = (1, 2, 3, 2, 3, 4, 5, 4)
print(tupleC.count(4))
print("\n")


dictA = {}
print(type(dictA))
dictA["name"] = "ranshen"
dictA["age"] = 29
dictA["pos"] = "programer"
print(dictA)
print(len(dictA))
print(dictA["name"])
dictA["name"] = "冉申"
print(dictA)
print("\n")


print(dictA.keys())
print(dictA.values())
print(dictA.items())
for item in dictA.items():
    print(item)
print("\n")


for key, value in dictA.items():
    print(f"{key} == {value}")
print("\n")


dictA.update({"love": "books"})
print(dictA)
dictA.update({"height": 1.80})
print(dictA)
print("\n")


del dictA["name"]
print(dictA)
dictA.pop("age")
print(dictA)
print("\n")


# 如何排序，按照key排序
print(sorted(dictA.items(), key=lambda d: d[0]))
print(dictA)
print("\n")


strA = "人生苦短"
strB = "我用python"
print(strA + strB)
print("\n")


listA = list(range(10))
listB = list(range(11, 20))
print(listA + listB)
print("\n")


print(strA * 3)
print(listA * 3)
print("生" in strA)
print("我" in strA)
print(22 in listA)
print(9 in listA)
dictA = {"name": "ranshen"}
print("age" in dictA)
print("name" in dictA)
