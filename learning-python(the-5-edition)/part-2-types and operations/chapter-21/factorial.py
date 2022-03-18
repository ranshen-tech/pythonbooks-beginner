# 计算factorial

from __future__ import print_function
from functools import reduce
from timeit import repeat
import math


def fact0(N):
    if N == 1:
        return N
    else:
        return N * fact0(N - 1)


def fact1(N):
    return N if N == 1 else N * fact1(N - 1)


def fact2(N):
    return reduce(lambda x, y: x * y, range(1, N + 1))


def fact3(N):
    res = 1
    for i in range(1, N + 1):
        res *= i
    return res


def fact4(N):
    return math.factorial(N)


# tests

print(fact0(6))
print(fact1(6))
print(fact2(6))
print(fact3(6))
print(fact4(6))
print("\n")

print(fact0(500) == fact1(500) == fact2(500) == fact3(500) == fact4(500))
print("\n")

for test in (fact0, fact1, fact2, fact3, fact4):
    print(test.__name__, min(repeat(stmt=lambda: test(500), number=20, repeat=3)))
print("\n")


def rev1(S):
    if len(S) == 1:
        return S
    else:
        return S[-1] + rev1(S[:-1])


def rev2(S):
    return "".join(reversed(S))


def rev3(S):
    return S[::-1]


l = ["a", "b", "c"]
L = [1, 2, 3]
print(rev2(l))
print(rev3(L))
print(rev3(l))
