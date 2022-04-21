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


def complexFunc(*args, **kwargs):
    """可选参数和关键字参数组合使用"""
    print(args)
    print(kwargs)


complexFunc(1, 2, 3, 4)
complexFunc(1, 2, 3, 4, name="ranshen")
complexFunc(age=29)
print("\n")


# 参数顺序（必选参数》默认参数〉可选参数（接受元组类型数据）》关键字参数（接收字典类型数据） ）


def sum(a, b):
    sum = a + b
    return sum


print(sum(10, 20))
rs = sum(10, 20)
print(rs)
print("\n")


def calComputer1(num):
    """计算累加值

    Args:
        num (_type_): 输入累加到哪个值
    """
    result = 0
    index = 1
    while index <= num:
        result += index
        index += 1
    return result


value = calComputer1(10)
print(type(value))
print(value)
print("\n")


def calComputer2(num):
    """计算累加值

    Args:
        num (_type_): 输入数字类型
    """
    l = []
    result = 0
    index = 1
    while index <= num:
        result += index
        index += 1
    l.append(result)
    return l


value = calComputer2(10)
print(type(value))
print(value)
print("\n")


def returnTuple():
    """返回元组类型的数据"""
    return 1, 2, 3


a = returnTuple()
print(type(a))
print(a)
print("\n")


def returnDict():
    """返回字典类型的数据"""
    return {"name": "ranshen"}


b = returnDict()
print(type(b))
print(b)
print("\n")


def fun1():
    print("------------fun1 start-----------")
    print("------------执行代码省略-------------")
    print("------------fun1 end-------------")


def fun2():
    print("-----------fun2 start------------")
    # 调用第一个函数
    fun1()
    print("-----------fun2 end--------------")


fun2()
print("\n")


def sumFunc(*args):
    """接收n个参数

    Returns:
        _type_: 参数和(int)
    """
    sum = 0
    for item in args:
        sum += item
    return sum


result = sumFunc(4, 5, 6, 7, 8, 9, 10)
print(f"result = {result}")
print("\n")


def process_func(container):
    """找出传入的列表或元组的奇数位对应的元素
    并返回新的列表
    """
    newlist = []
    index = 1
    for i in container:
        if index % 2 == 1:
            newlist.append(i)
        index += 1
    return newlist


print(process_func([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(process_func(tuple(range(10))))
print("\n")
