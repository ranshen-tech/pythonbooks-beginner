X = 88
print(X)


def func():
    global X
    X = 99
    return X


print(func())
print(X)
print("\n")


# Programming: 最少化全局变量

X = 99


def func1():
    global X
    X = 88
    return X


def func2():
    global X
    X = 77
    return X


print(func2())
print(func1())
print("\n")
