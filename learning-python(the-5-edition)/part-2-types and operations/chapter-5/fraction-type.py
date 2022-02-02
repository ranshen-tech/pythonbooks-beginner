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


# 分数转换和混用类型
print((2.5).as_integer_ratio())

f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)
print(x)
print(x + z)

print(float(x))
print(float(z))
print(float(x + z))
print(17 / 6)

print(Fraction.from_float(1.75))
print(Fraction(*(1.75).as_integer_ratio()))

print("\n")
print(x)
print(x + 2)
print(x + 2.0)
print(x + (1.0 / 3))
print(x + (4.0 / 3))
print(x + Fraction(4, 3))
