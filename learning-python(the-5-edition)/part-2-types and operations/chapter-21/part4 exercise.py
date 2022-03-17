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
