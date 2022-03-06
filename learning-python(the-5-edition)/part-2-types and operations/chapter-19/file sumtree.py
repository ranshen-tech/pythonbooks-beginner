# 处理任意结构


def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))
print(sumtree([1, [2, [3, [4, [5]]]]]))
print(sumtree([[[[[1], 2], 3], 4], 5]))


# recursion VS queue & stack


def sumtree(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items.extend(front)
    return tot


def sumtree(L):
    tot = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
    return tot


print("\n")


# if state not in visited:
#     visited.add(state)
#     ...proceed...


# visited.add(front)
# ...proceed...
# items.extend([x for x in front if x not in visited])

import sys

print(sys.getrecursionlimit())
print(sys.setrecursionlimit(10000))
# print(help(sys.setrecursionlimit))
