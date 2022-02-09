# 字典的基本操作
D = {"spam": 2, "ham": 1, "eggs": 3}
print(D["spam"])
print(D)
print("\n")

print(len(D))
print("ham" in D)
print(list(D.keys()))
print("\n")


# 原位置修改字典
print(D)
D["ham"] = ["grill", "bake", "fry"]
print(D)
del D["eggs"]
print(D)
D["brunch"] = "Bacon"
print(D)
print("\n")


# 其他字典方法
D = {"spam": 2, "ham": 1, "eggs": 3}
print(list(D.values()))
print(list(D.items()))
print("\n")

print(D.get("spam"))
print(D.get("toast"))
print(D.get("toast", 88))
print(D.get("toast"))
print(D)
print("\n")

print(D)
D2 = {"toast": 4, "muffin": 5}
D.update(D2)
print(D2)
print(D)
print("\n")

print(D)
print(D.pop("muffin"))
print(D)
print(D.pop("toast"))
print(D)
print("\n")

L = ["aa", "bb", "cc", "dd"]
print(L.pop())
print(L)
print(L.pop(1))
print(L)
print("\n")


# 示例：电影数据库
table = {"1975": "Holy Grail", "1979": "Life of Brian", "1983": "The Meaning of Life"}

year = "1983"
movie = table[year]
print(movie)
for year in table:
    print(year + "\t" + table[year])
print("\n")


# 预习：将值映射为键
table = {"Holy Grail": "1975", "Life of Brian": "1979", "The Meaning of Life": "1983"}
print(table["Holy Grail"])

print(list(table.items()))
print([title for (title, year) in table.items() if year == "1975"])
print("\n")

print(table)
K = "Holy Grail"
print(table[K])

V = "1975"
print([key for (key, value) in table.items() if value == V])
print([key for key in table.keys() if table[key] == V])
print("\n")


# 用字典模拟灵活的列表：整数键
D = [[0] * 3]
# D[99] = "spam"
print(D)
print("\n")

D = {}
D[99] = "spam"
print(D)
print(D[99])
print("\n")

table = {1975: "Holy Grail", 1979: "Life of Brian", 1983: "The Meaning of Life"}
print(table[1975])
print(list(table.items()))
