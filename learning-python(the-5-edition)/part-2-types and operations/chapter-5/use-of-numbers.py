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
