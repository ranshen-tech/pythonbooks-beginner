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
