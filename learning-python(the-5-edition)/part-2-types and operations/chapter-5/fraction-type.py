# 分数基础知识
import decimal
from fractions import Fraction
from decimal import Decimal

x = Fraction(1, 3)
y = Fraction(4, 6)

print(x)
print(y)

print(x + y)
print(x - y)
print(x * y)

print(Fraction("0.25"))
print(Fraction("1.25"))
print(Fraction("0.25") + Fraction("1.25"))


# 分数和小数中的数值精度
a = 1 / 3.0
b = 4 / 6.0
print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)

print(0.1 + 0.1 + 0.1 - 0.3)
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))
print(Fraction(1, 10) * 3 - Fraction(3, 10))

print(Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3"))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))

print(Decimal("0.1") * 3 - Decimal("0.3"))

print(1 / 3)
print(Fraction(1, 3))
decimal.getcontext().prec = 2
print(Decimal(1) / Decimal(3))

print((1 / 3) + (6 / 12))
print(Fraction(6, 12))

print(Fraction(1, 3) + Fraction(6, 12))

print(Decimal(str(1 / 3)) + Decimal(str(6 / 12)))
print(Fraction(1000, 12345677890))
