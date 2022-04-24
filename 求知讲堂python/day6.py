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
print("\n")


# all()判断给定的可迭代参数是否都为True，空元组、空列表返回True
print(bool([]))
print(all([0]))
print(all([1]))
print(all([]))
print(all(()))
print(all([1, 2, 3, False, True]))
print(all([[]]))
print(all([]))
print("\n")


# any()判断给定的可迭代参数是否全部为False，则返回False， 有一个是True则返回True
print(any([]))
print(any([[]]))
print(any([0]))
print(any([1]))
print(any([1, 0]))
print(any(["", 0, False, 1]))
print("\n")


# sort是应用在list上的排序方法，sorted可对所有可迭代对象排序，sorted返回的是新的list
l = [1, 2, 3, 5, 4, 1]
# list排序方法，直接修改原始对象，元组不可以
l.sort()
print(l)

print("排序之前的l", l)
li = sorted(l, reverse=True)
print("排序之后的l", li)
print(f"排序之后的li {li}")
print(f"排序之后的l{l}")
print("\n")


t = (1, 2, 5, 3, 1)
print(t)
tup = sorted(t)
print(tup)
print("\n")


a = [1, 2, 3, 4, 5]
a.reverse()
print(a)
print("\n")


# zip()将可迭代对象作为参数，将对象中对应的元素打包成元组，然后返回由这些元组组成的列表
s1 = ["a", "b", "c"]
s2 = ["你", "我", "它"]
print(zip(s1))
print(list(zip(s1)))
print(list(zip(s1, s2)))


def books_info():
    """zip函数的使用"""
    # 存储所有图书信息
    books = []
    book_id = input("请输入编号")
    book_name = input("请输入书名")
    book_pos = input("请输入书的位置")

    id_list = book_id.split()
    name_list = book_name.split()
    pos_list = book_pos.split()

    # 打包处理
    books_info = list(zip(id_list, name_list, pos_list))
    print(books_info)

    # 遍历图书信息进行存储
    for book_item in books_info:
        dict_info = {"编号": book_item[0], "书名": book_item[1], "位置": book_item[2]}
        #  将字典对象添加到列表
        books.append(dict_info)

    for item in books:
        print(item)


# books_info()
print("\n")
