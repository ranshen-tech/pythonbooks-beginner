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
