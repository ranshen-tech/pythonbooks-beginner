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
