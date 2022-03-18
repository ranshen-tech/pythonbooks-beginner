# timing tool

import sys, timer2

reps = 10000
repslist = range(reps)

from math import sqrt


def mathMod():
    for i in repslist:
        res = sqrt(i)
    return res


def powCall():
    for i in repslist:
        res = pow(i, 0.5)
    return res


def powExpr():
    for i in repslist:
        res = i**0.5
    return res


print(sys.version)
for test in (mathMod, powCall, powExpr):
    elapsed, result = timer2.bestoftotal(test, _reps1=3, _reps=1000)
    print("%s: %.5f => %s" % (test.__name__, elapsed, result))
print("\n")


def dictcomp(I):
    return {i: i for i in range(I)}


def dictloop(I):
    new = {}
    for i in range(I):
        new[i] = i
    return new


print(dictcomp(10))
print(dictloop(10))
print("\n")

from timer2 import total, bestof

print(bestof(dictcomp, 10000)[0])
print(bestof(dictloop, 10000)[0])
print("\n")

print(bestof(dictcomp, 100000)[0])
print(bestof(dictloop, 100000)[0])
print("\n")

print(bestof(dictcomp, 1000000)[0])
print(bestof(dictloop, 1000000)[0])
print("\n")

print(bestof(dictcomp, 1000000, _reps=50)[0])
print(bestof(dictloop, 1000000, _reps=50)[0])
