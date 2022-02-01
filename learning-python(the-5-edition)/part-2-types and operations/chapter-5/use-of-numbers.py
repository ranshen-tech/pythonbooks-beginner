print(int(3.8))
print(float(3))
print(3 == 3.0)

# 变量与基础表达式
a = 3
b = 4

print(a + 1, a - 1)
print(b * 3, b / 2)
print(a % 2, b**2)
print(2 + 4.0, 2.0**b)

print(b / 2 + a)
print(b / (2.0 + a))
print(b // 2 + a)


# 数值的显示格式
num = 1 / 3.0
print(num)

print("%e" % num)
print("%4.2f" % num)
print("{0:4.2f}".format(num))

print(repr("spam"))
print(str("spam"))


# 普通比较与链式比较
print(1 < 2)
print(2.0 >= 1)
print(2.0 == 2.0)
print(2.0 != 2.0)

X = 2
Y = 4
Z = 6

print(X < Y < Z)
print(X < Y and Y < Z)

print(X < Y > Z)
print(X < Y and Y > Z)

print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)

# same as: 1 == 2 and 2 < 3
# not same as: False < 3 (which means 0 < 3)
print(1 == 2 < 3)

print(1.1 + 2.2 == 3.3)
print(1.1 + 2.2)
print(int(1.1 + 2.2) == int(3.3))


# 除法：经典除法、向下取整除法和真除法
print(10 / 4)
print(10 / 4.0)
print(10 // 4)
print(10 // 4.0)

X = Y // Z
print(X)
X = Y / Z
print(X)


# 向下取整除法 VS 截断除法
import math

print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))

print(5 / 2, 5 / -2)
print(5 // 2, 5 // -2)
print(5 / 2.0, 5 / -2.0)
print(5 // 2.0, 5 // -2.0)
print(int(2.5), int(-2.5))

print(5 / -2)
print(5 // -2)
print(math.trunc(5 / -2))


# 为什么截断很重要
print(5 / 2, 5 / 2.0, 5 / -2.0, 5 / -2)
print(5 // 2, 5 // 2.0, 5 // -2, 5 // -2.0)
print(9 / 3, 9.0 / 3, 9 // 3, 9 // 3.0)


# 复数
print(1j * 1j)
print(2 + 1j * 3)
print((2 + 1j) * 3)


# 十六进制、八进制和二进制：字面量与转换
print(0o1, 0o0, 0o377)
print(0x01, 0x10, 0xFF)
print(0b1, 0b10000, 0b11111111)

print(0xFF, (15 * (16**1)) + (15 * (16**0)))
print(0x2F, (2 * (16**1)) + (15 * (16**0)))
print(0xF, 0b1111, (1 * (2**3) + 1 * (2**2) + 1 * (2**1) + 1 * (2**0)))

print(oct(64), hex(64), bin(64))

print(64, 0o100, 0x40, 0b1000000)
print(int("64"), int("100", 8), int("40", 16), int("1000000", 2), int("64", 10))
print(int("0x40", 16), int("0b1000000", 2))

print(eval("64"), eval("0o100"), eval("0x40"), eval("0b1000000"))

print("{0:o}, {1:x}, {2:b}".format(64, 64, 64))
print("%o, %x, %x, %X" % (64, 64, 255, 255))

print(0o1, 0o20, 0o377)

X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
print(X)
print(oct(X))
print(bin(X))


# 按位操作
x = 1
print(x)
print(x << 2)
print(int("0100", 2))
print(x | 2)
print(x & 1)

X = 0b0001
print(X << 2)
print(bin(X << 2))
print(bin(X | 0b010))
print(bin(X & 0b1))

X = 0xFF
print(bin(X))
print(X ^ 0b10101010)
print(int("1010101", 2))
print(hex(85))

X = 99
print(bin(X), X.bit_length(), len(bin(X)) - 2)
print(bin(256), (256).bit_length(), len(bin(256)) - 2)


# 其他内置数值工具
import math

print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144), math.sqrt(2))
print(pow(2, 4), 2**4, 2.0**4.0)
