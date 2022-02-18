# 基础示例
if 1:
    print("true")
print("\n")

if not 1:
    print("true")
else:
    print("false")
print("\n")


# 多路分支
x = "killer rabbit"
if x == "roger":
    print("shave and a haircut")
elif x == "bugs":
    print("what's up doc?")
else:
    print("run away! Run away!")
print("\n")

choice = "ham"
print({"spam": 1.25, "ham": 1.99, "eggs": 0.99, "bacon": 1.10}[choice])
print("\n")

if choice == "spam":
    print(1.25)
elif choice == "ham":
    print(1.99)
elif choice == "eggs":
    print(0.99)
elif choice == "bacon":
    print(1.10)
else:
    print("Bad choice")
print("\n")


# 处理选择语句的默认情况
branch = {"spam": 1.25, "ham": 1.99, "eggs": 0.99}
print(branch.get("spam", "Bad choice"))
print(branch.get("bacon", "Bad choice"))
print("\n")

choice = "bacon"
if choice in branch:
    print(branch[choice])
else:
    print("Bad choice")
print("\n")

try:
    print(branch[choice])
except KeyError:
    print("Bad choice")
print("\n")


# 处理更大规模的活动
def function():
    pass


def default():
    pass


branch = {"spam": lambda: ..., "ham": function, "eggs": lambda: ...}
branch.get(choice, default)()
