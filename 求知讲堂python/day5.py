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
