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
print("\n")


# 对稀疏数据结构使用字典：用元组做键
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

X = 2
Y = 3
Z = 4
print(Matrix[X, Y, Z])
print(Matrix)
print("\n")

# print(Matrix[(2, 3, 6)])


# 避免键不存在错误
if (2, 3, 6) in Matrix:
    print(Matrix[(2, 3, 6)])
else:
    print(0)

try:
    print(Matrix[(2, 3, 6)])
except KeyError:
    print(0)

print(Matrix.get((2, 3, 4), 0))
print(Matrix.get((2, 3, 6), 0))
print("\n")

# 字典的嵌套
rec = {}
rec["name"] = "Bob"
rec["age"] = 40.5
rec["job"] = "developer/manager"

print(rec)
print(rec["name"])
print("\n")

rec = {
    "name": "Bob",
    "jobs": ["developer", "manager"],
    "web": "www.bobs.org/?Bob",
    "home": {"state": "Overworked", "zip": 12345},
}
print(rec)
print(rec["name"])
print(rec["jobs"])
print(rec["jobs"][1])
print(rec["home"]["zip"])
print("\n")

db = []
db.append(rec)
print(db)
print(db[0]["jobs"])
print("\n")

db = {}
db["bob"] = rec
print(db)
print(db["bob"]["jobs"])
print("\n")


# 创建字典的其他方式
{"name": "Bob", "age": 40}

D = {}
D["name"] = "Bob"
D["age"] = 40

a = dict(name="Bob", age=40)
print(a)
b = dict([("name", "Bob"), ("age", 40)])
print(b)
print("\n")

print(list(b.keys()))
print(dict(zip(b.keys(), b.values())))
print("\n")

a = [1, 2, 3]
b = [4, 5, 6]
print(zip(a, b))
print(list(zip(a, b)))
c = dict(list(zip(a, b)))
print(c)
print("\n")

c = {"a": 0, "b": 0}
c["c"] = 0
print(c)
c = dict.fromkeys(["a", "b", "c"], 1)
print(c)
print("\n")

a = dict([("name", "bob"), ("age", 40)])
print(a)
print("\n")


# 请留意：字典 vs 列表
L = ["Bob", 40.5, ["dev", "mgr"]]
print(L[0])
print(L[1])
print(L[2][1])
print("\n")

D = {"name": "Bob", "age": 40.5, "jobs": ["dev", "mgr"]}
print(D["name"])
print(D["age"])
print(D["jobs"][1])
print("\n")

D = dict(name="Bob", age=40.5, jobs=["dev", "mgr"])
print(D["name"])
D["jobs"].remove("mgr")
print(D)
print("\n")

D = {}
D["state1"] = True
print("state1" in D)
S = set()
S.add("state1")
print(S)
print("state1" in S)
print("\n")


# Python 3.X 和 2.7中的字典推导
print(list(zip(["a", "b", "c"], [1, 2, 3])))
