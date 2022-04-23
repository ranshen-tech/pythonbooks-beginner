print(abs(-32))
print("\n")


# round()对浮点数取近似值
print(round(2.6))
print(round(2.5))
print(round(2.4))
print(round(-2.6))
print(round(-2.4))
print(round(2.66, 1))
print("\n")


# pow()求幂运算
print(pow(3, 3))
print(3**3)
print("\n")


# max()求最大值
print(max(1, 3))
print(max([1, 2, 3], [3, 2, 1], [4, 0, 0]))
print(max((1, 3, 4), (5,)))
print("\n")


# sum()求和
print(sum(range(50)))
print(sum(range(50), 3))
print("\n")


# eval()动态执行字符串表达式,并返回表达式的值
a, b, c = 1, 2, 3
print(eval("a + b + c"))
print(eval("a + b, c"))
print(type(eval("a+b+c")))
print(eval("a* b + c -30"))
print("\n")


def test_func():
    print("我执行了吗？")


test_func()
eval("test_func()")
print(eval("test_func"))
print(eval("a+b"))
print("\n")


print(bin(10))
print(hex(23))
print(hex(10))
print("\n")


t = (1, 2, 3, 4)
print(type(t))
l = list(t)
print(type(l))
print(l)
l.append("强制转换成功")
print(l)
print("\n")


d = dict()
print(type(d))
print(d)
d = dict(name="ranshen", age=29)
print(d)
