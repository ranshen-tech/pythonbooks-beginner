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


def f1():
    X = 88

    def f2():
        print(X)

    return f2


action = f1()
action()
print("\n")


# factory function & closure


def maker(N):
    def action(X):
        return X**N

    return action


f = maker(2)
print(f)
print(f(3))
print(f(4))
print("\n")

g = maker(3)
print(g(4))
print(f(4))
print("\n")
print(maker(3)(4))
