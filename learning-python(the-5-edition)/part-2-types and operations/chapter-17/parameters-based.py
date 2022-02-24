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
