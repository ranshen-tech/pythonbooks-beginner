# def statement

# def name(arg1, arg2,...argN):
#     statements


# def name(arg2, arg2...argN):
#     ...
#     return value


# if test:
#     def func():
#         ...
# else:
#     def func():
#         ...
# ...
# func()


# othername = func
# othername()

# def func():
#     ...
# func()
# func.attr = value


# Example1


def times(x, y):
    return x * y


print(times(2, 4))
print("\n")

x = times(3.14, 4)
print(x)
print("\n")

print(times("Ni", 4))
print("\n")


# Example2


def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


def intersect2(seq1, seq2):
    res = [x for x in seq1 if x in seq2]
    return res


s1 = "SPAM"
s2 = "SCAM"
print(intersect(s1, s2))
print(intersect2(s1, s2))
print("\n")

x = intersect2([1, 2, 3], (1, 4))
print(x)
print("\n")

print(intersect([1, 2, 3], []))
print("\n")


# Action-scope example

X = 99


def func(Y):
    Z = X + Y
    return Z


print(func(1))


import builtins

print(dir(builtins))
print("\n")
