X = set("spam")
Y = {"h", "a", "m"}

print(X, Y)

print(X & Y)
print(X | Y)
print(X - Y)
print(X > Y)

print({n**2 for n in [1, 2, 3, 4]})

print(list(set([1, 2, 1, 3, 1])))
print(set([1, 2, 1, 3, 1]))
print(set("spam") - set("ham"))
print(set("spam") == set("asmp"))

print("p" in set("spam"), "p" in "spam", "ham" in ["eggs", "spam", "ham"])

print(1 / 3)
print((2 / 3) + (1 / 2))

import decimal

d = decimal.Decimal("3.141")
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal("1.00") / decimal.Decimal("3.00"))

from fractions import Fraction

f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))

print(1 > 2, 1 < 2)
print(bool("spam"))

X = None
print(X)
L = [None] * 100
print(L)


# 如何破坏代码的灵活性
print(type(L))
print(type(type(L)))

if type(L) == type([]):
    print("yes")
if type(L) == list:
    print("yes")
if isinstance(L, list):
    print("yes")


# 用户定义的类
class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay *= 1.0 + percent


bob = Worker("Bob Smith", 50000)
sue = Worker("Sue Jones", 60000)
print(bob.lastName())
print(sue.lastName())
sue.giveRaise(0.10)
print(sue.pay)

a = (1, 2)
b = (3, 4)
print(a, b)
print(a + b)
