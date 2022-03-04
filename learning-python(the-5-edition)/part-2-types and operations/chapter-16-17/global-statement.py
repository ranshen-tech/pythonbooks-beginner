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
print("\n")


def maker(N):
    return lambda X: X**N


h = maker(3)
print(h(4))
print("\n")


def f1():
    x = 88

    def f2(x=x):
        print(x)

    f2()


f1()
print("\n")


def f1():
    x = 88
    f2(x)


def f2(x):
    print(x)


f1()
print("\n💖")


def f1():
    x = 88

    def f2(x=x):
        print(x)

    f2()


f1()
print("\n")


def f1():
    x = 88
    f2(x)


def f2(x):
    print(x)


f1()
print("\n")


# nested scope & fault参数 & lambda
def func():
    x = 4
    action = lambda n: x**n
    return action


x = func()
print(x(2))
print("\n")


def func():
    x = 3
    action = lambda n, x=x: x**n
    return action


x = func()
print(x(2))
print("\n")


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i**x)
    return acts


acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](3))
print(acts[3](2))
print(acts[4](2))
print("\n")


def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i**x)
    return acts


acts = makeActions()
print(acts[0](2))
print(acts[1](2))
print(acts[2](2))
print(acts[3](2))
print(acts[4](2))
