# 代码块分隔符：缩进规则
x = 1
if x:
    y = 2
    if y:
        print("block2")
    print("block1")
print("block0")
print("\n")

x = "SPAM"
if "rubbery" in "shrubbery":
    print(x * 8)
    x += "NI"
    if x.endswith("NI"):
        x *= 2
        print(x)
print("\n")


# 语句分隔符：行与行间连接符
L = ["Good", "Bad", "Ugly"]
print("\n")
