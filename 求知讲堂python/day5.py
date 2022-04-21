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
