major = "计算机信息管理"
name = "shawn ran"


def print_info():
    name = "shawn"
    print(f"name is {name}, major is {major}.")


def test_method():
    name = "冉申"
    print(name, major)


def change_global():
    """修改全局变量"""
    global major
    major = "金融工程"


change_global()
print(major)
print_info()
test_method()
print("\n")


a = 1


def func(x):
    print(f"x的地址:{id(x)}")
    x = 2
    print(f"x的值修改后的地址:{id(x)}")


print(f"a的地址:{id(a)}")
func(a)
print("\n")


l = []


def test_renc(parms):
    l.append(1)
    print(f"{l}\n")
    print(id(parms))
    print(f"内部的l{parms}")


# 在python中，万物皆对象，实参传递的就是对象的引用，这句话非常重要‼️
print(id(l))
test_renc(l)
print(f"外部的变量对象{l}")
print("\n")


def computer(x, y):
    """计算参数的和

    Args:
        x (_type_): int
        y (_type_): int
    """
    return x + y


print(computer(2, 3))
print("\n")


M = lambda x, y: x + y
# 通过变量去调用匿名函数
print(M(23, 19))
print("\n")


result = lambda a, b, c: a * b * c
print(result(12, 34, 2))
print("\n")


# def 三元运算():
#     if a:
#         b
#     else:
#         c


# def 三元运算():
#     b if a else c

greater = lambda x, y: x if x > y else y
print(greater(3, 5))
print(greater(6, 2))
print("\n")


age = 22
print("可以参军" if age > 18 else "继续上学")
print("\n")


# 直接调用
result = (lambda x, y: x if x > y else y)(16, 12)
print(result)
varRs = lambda x: (x**2) + 890
print(varRs(10))
