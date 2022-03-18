# 1 basic


def func(x):
    print(x)


func("spam")
func(42)
func([1, 2, 3])
func({"food": "spam"})
print("\n")


# 2 parameter


def adder(x, y):
    return x + y


print(adder(2.2, 3.3))
print(adder("spam", "eggs"))
print(adder(["a", "b"], ["c", "d"]))
print("\n")


# 3 可变长parameter


def adder1(*args):
    print("adder1", end=" ")
    if type(args[0]) == type(0):
        sum = 0
    else:
        sum = args[0][:0]
    for arg in args:
        sum = sum + arg
    return sum


def adder2(*args):
    print("adder2", end=" ")
    sum = args[0]
    for next in args[1:]:
        sum += next
    return sum


for func in (adder1, adder2):
    print(func(2, 3, 4))
    print(func("spam", "eggs", "toast"))
    print(func(["a", "b"], ["c", "d"], ["e", "f"]))
print("\n")


# 4 关键字parameter


def adder(good=1, bad=2, ugly=3):
    return good + bad + ugly


print(adder())
print(adder(5))
print(adder(5, 6))
print(adder(5, 6, 7))
print(adder(ugly=7, good=6, bad=5))
print("\n")


# Second part solutions


def adder1(*args):
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot


def adder2(**args):
    argskeys = list(args.keys())
    tot = args[argskeys[0]]
    for key in argskeys[1:]:
        tot += args[key]
    return tot


def adder3(**args):
    args = list(args.values())
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot


def adder4(**args):
    return adder1(*args.values())


print(adder1(1, 2, 3), adder1("aa", "bb", "cc"))

print(adder2(a=1, b=2, c=3), adder2(a="aa", b="bb", c="cc"))

print(adder3(a=1, b=2, c=3), adder3(a="aa", b="bb", c="cc"))

print(adder4(a=1, b=2, c=3), adder4(a="aa", b="bb", c="cc"))
print("\n")


# 5, 6 dict tools


def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new


def addDict(d1, d2):
    new = {}
    for key in d1.keys():
        new[key] = d1[key]
    for key in d2.keys():
        new[key] = d2[key]
    return new


d = {1: 1, 2: 2}
print(d.copy())
e = copyDict(d)
print(e)

d[2] = "?"
print(d)
print(e)
print("\n")

x = {1: 1}
y = {2: 2}
z = addDict(x, y)
print(z)

x.update(y)
print(x)
print("\n")


# 7 more parameter match example


def f1(a, b):
    print(a, b)


def f2(a, *b):
    print(a, b)


def f3(a, **b):
    print(a, b)


def f4(a, *b, **c):
    print(a, b, c)


def f5(a, b=2, c=3):
    print(a, b, c)


def f6(a, b=2, *c):
    print(a, b, c)


f1(1, 2)
f1(b=2, a=1)
print("\n")

f2(1, 2, 3)
print("\n")

f3(1, x=2, y=3)

f4(1, 2, 3, x=2, y=3)
print("\n")

f5(1)
f5(1, 4)
print("\n")

f6(1)
f6(1, 3, 4)
print("\n")


# 9 iteration and comprehension

import math

values = [2, 4, 9, 16, 25]
res = []
for x in values:
    res.append(math.sqrt(x))
print(res)

print(list(map(math.sqrt, values)))

print([math.sqrt(x) for x in [2, 4, 9, 16, 25]])

print(list((math.sqrt(x) for x in values)))
print("\n")


# recursion function


def countdown(N):
    if N == 0:
        print("stop")
    else:
        print(N, end=" ")
        countdown(N - 1)


countdown(5)
countdown(20)
print("\n")

# Nonrecursive options
print(list(range(5, 0, -1)))
print("\n")

# On 3.X only:
t = [print(i, end=" ") for i in range(5, 0, -1)]
print("\n")

t = list(map(lambda x: print(x, end=" "), range(5, 0, -1)))
print("\n")


def countdown2(N):
    if N == 0:
        yield "stop"
    else:
        yield N
        for x in countdown2(N - 1):
            yield x


print(list(countdown2(5)))
print("\n")
