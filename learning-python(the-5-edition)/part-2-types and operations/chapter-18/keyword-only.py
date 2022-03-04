def keywordonly(a, *b, c):
    print(a, b, c)


keywordonly(1, 2, c=3)
keywordonly(a=1, c=3)
# keywordonly(1, 2, 3)
print("\n")


def keywordonly(a, *, b, c):
    print(a, b, c)


keywordonly(1, c=3, b=2)
keywordonly(c=3, b=2, a=1)
# keywordonly(1, 2, 3)
# keywordonly(1)
print("\n")


def keywordonly(a, *, b="spam", c="ham"):
    print(a, b, c)


keywordonly(1)
keywordonly(1, c=3)
keywordonly(a=1)
keywordonly(c=3, b=2, a=1)
# keywordonly(1, 2)
print("\n")


def kwonly(a, *, b, c="spam"):
    print(a, b, c)


kwonly(1, b="eggs")
# kwonly(1, c="eggs")
# kwonly(1, 2)
print("\n")


def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)


kwonly(3, c=4)
kwonly(3, c=4, b=5)
# kwonly(3)
# kwonly(1, 2, 3)
print("\n")


# def kwonly(a, **pargs, b, c):
# def kwonly(a, **, b, c):

# def f(a, *b, **d, c=6):
# print(a,b, c,d)


def f(a, *b, c=6, **d):
    print(a, b, c, d)


f(1, 2, 3, x=4, y=5)
f(1, 2, 3, x=4, y=5, c=7)
f(1, 2, 3, c=7, x=4, y=5)
print("\n")


def f(a, c=6, *b, **d):
    print(a, b, c, d)


f(1, 2, 3, 4)
f(1, 2, 3, x=4)
print("\n")

# 💖


def f(a, *b, c=6, **d):
    print(a, b, c, d)


f(1, *(2, 3), **dict(x=4, y=5))
f(1, *(2, 3), **dict(x=4, y=5), c=7)
f(1, *(2, 3), c=7, **dict(x=4, y=5))
f(1, c=7, *(2, 3), **dict(x=4, y=5))
f(1, *(2, 3), **dict(x=4, y=5, c=7))
print("\n")

#
# process(X, Y, Z)
# process(X, Y, notify=True)
# def process(*args, notify=False): ...


# min提神小例


def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


def min3(*args):
    tem = list(args)
    tem.sort()
    return tem[0]


print(min1(3, 4, 1, 2))
print(min2("bb", "aa"))
print(min3([2, 2], [1, 1], [3, 3]))
print("\n")


# 附加分


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y):
    return x < y


def greaterthan(x, y):
    return x > y


print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
print(minmax(greaterthan, 4, 2, 1, 5, 6, 3))
