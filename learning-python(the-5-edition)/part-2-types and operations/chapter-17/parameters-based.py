# 参数和共享引用


def f(a):
    a = 99


b = 88
print(f(b))
f(b)
print(b)
print("\n")


def changer(a, b):
    a = 2
    b[0] = "spam"
    return a, b


X = 1
L = [1, 2]
changer(X, L)
print(X, L)
print("\n")

X = 1
a = X
a = 2
print(X)
print("\n")

L = [1, 2]
b = L
b[0] = "spam"
print(L)
print("\n")


# 避免修改可变参数
L = [1, 2]


def changer(a, b):
    b = b[:]
    a = 2
    b[0] = "spam"


# changer(X, tuple(L))
print("\n")


# 模拟输出参数和多重结果


def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y


X = 1
L = [1, 2]
X, L = multiple(X, L)
print(X, L)
print("\n")

# def f(T):
# a, (b, c) = T


def f(a, b, c):
    print(a, b, c)


f(1, 2, 3)
print("\n")

f(c=3, b=2, a=1)
f(1, c=3, b=2)
print("\n")

# func(name="Bob", age=40, job="dev")


# 默认值参数


def f(a, b=2, c=3):
    print(a, b, c)


f(1)
f(a=1)
print("\n")

f(1, 4)
f(1, 4, 5)
f(1, c=6)
print("\n")


# 混合使用关键字参数和默认值参数


def func(spam, eggs, toast=0, ham=0):
    print((spam, eggs, toast, ham))


func(1, 2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast=1, eggs=2, spam=3)
func(1, 2, 3, 4)
print("\n")


# function define:收集参数


def f(*args):
    print(args)


f()
f(1)
f(1, 2, 3, 4)
print("\n")


def f(**args):
    print(args)


f()
f(a=1, b=2)
print("\n")


def f(a, *pargs, **kargs):
    print(a, pargs, kargs)


f(1, 2, 3, x=1, y=2)
print("\n")


# function call: unpack the parameters


def func(a, b, c, d):
    print(a, b, c, d)


args = (1, 2)
args += (3, 4)
print(args)
func(*args)
print("\n")

args = {"a": 1, "b": 2, "c": 3}
args["d"] = 4
func(**args)
print("\n")


func(*(1, 2), **{"d": 4, "c": 3})
func(1, *(2, 3), **{"d": 4})
func(1, c=3, *(2,), **{"d": 4})
func(1, *(2, 3), d=4)
func(1, *(2,), c=3, **{"d": 4})
print("\n")


# 泛化地使用函数

# if sometest:
# action, args = func1, (1,)
# else:
# action, args = func2, (1, 2, 3)

args = (2, 3)
args += (4,)
print(args)
# func(*args)
print("\n")
