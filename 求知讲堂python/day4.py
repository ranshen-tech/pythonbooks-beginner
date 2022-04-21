print(f"冉申的身高是{180}")
print(f"冉申的体重是{63}")
print("冉申的爱好是读书")
print("冉申的专业是计算机")
print("\n")


def printInfo():
    """
    这个函数是用来打印冉申的个人信息，
    是信息的组合
    """
    print(f"冉申的身高是{180}")
    print(f"冉申的体重是{63}")
    print("冉申的爱好是读书")
    print("冉申的专业是计算机")
    print("\n")


printInfo()


def printInfo(name, height, weight, hobby, pro):
    """
    更加灵活，个性化定制个人信息
    """
    print(f"{name}的身高是{height}")
    print(f"{name}的体重是{weight}")
    print(f"{name}的爱好是{hobby}")
    print(f"{name}的专业是{pro}")


printInfo("冉总", 178, 62, "阅读", "计算机")
print("\n")
