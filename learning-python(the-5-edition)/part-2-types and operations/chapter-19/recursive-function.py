# 用recursion求和


def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


print(mysum([1, 2, 3, 4, 5]))
print("\n")


def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


print(mysum([1, 2, 3, 4, 5]))
print("\n")


# 编码替代方案


def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])


print(mysum([1]))
print(mysum([1, 2, 3, 4, 5]))
print("\n")


def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])


print(mysum([1]))
print(mysum([1, 2, 3, 4, 5]))
print(mysum(("s", "p", "a", "m")))
print(mysum(["spam", "ham", "eggs"]))
print("\n")


def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)


print(mysum([1]))
print(mysum([1, 2, 3, 4, 5]))
print(mysum(("s", "p", "a", "m")))
print(mysum(["spam", "ham", "eggs"]))
print("\n")


def mysum(L):
    if not L:
        return 0
    return nonempty(L)


def nonempty(L):
    return L[0] + mysum(L[1:])


print(mysum([1.1, 2.2, 3.3, 4.4]))
print("\n")


# loop statement & recursion


L = [1, 2, 3, 4, 5]
sum = 0
while L:
    sum += L[0]
    L = L[1:]

print(sum)
print("\n")


for x in L:
    sum += x

print(sum)
print("\n")


# 处理任意结构
