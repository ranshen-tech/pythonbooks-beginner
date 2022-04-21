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
print("---------------------------------")
printInfo("ShawnRan", 180, 63, "投机", "计算机金融工程")
print("\n")


def sum(a, b):
    """
    自定义的加法函数
    """
    sum = a + b
    print(sum)


sum(20, 15)
print("\n")


def sum1(a=20, b=30):
    """
    默认参数
    """
    print(f"默认参数使用={a+b}")


sum1()
sum1(1)
print("\n")


def sum2(a, b=20):
    """
    默认参数始终在参数列表尾部
    """
    print(f"默认参数使用={a+b}")


sum2(2, 4)
sum2(5)
print("\n")


# 可变参数(当参数的个数不确定时使用，比较灵活)
def getComputer(*args):
    """
    可变长的参数类型
    计算累加和
    """
    # print(args)
    result = 0
    for item in args:
        result += item
    print(f"result={result}")


# 打印出来的都是元组类型的数据
# getComputer((1, 2, 3, 4, 5, 6))
getComputer(1)
getComputer(1, 2, 3)
print("\n")


# 关键字参数（**来定义,参数关键字是一个字典类型,key是一个字符串）
def keyFunc(**keywordargs):
    """参数关键字是一个字典类型,key是一个字符串"""
    print(keywordargs)


# keyFunc(1, 2, 4) 这样是不可以的
dictA = {"name": "ranshen", "age": 29}
# keyFunc(dictA) 这样也是不可以的
keyFunc(**dictA)
keyFunc(name="ranshen", age=29)
keyFunc()
print("\n")
