# 分数基础知识
from fractions import Fraction

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

print(1 / 3 + 2 / 3)
