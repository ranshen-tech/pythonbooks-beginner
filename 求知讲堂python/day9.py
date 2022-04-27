class Person(object):
    # 定义一个私有化属性，属性前面加两个下划线
    __age = 18


class Person:
    __hobby = "dance"

    def __init__(self):
        # 私有化之后就不能在类外部访问了
        self.__name = "冉申"
        self.age = 30

    def __str__(self):
        return f"{self.__name}的年龄是{self.age},爱好是{Person.__hobby}"

    def change_value(self):
        Person.__hobby = "sing"


rs = Person()
# print(rs.name)
print(rs.age)
print(rs)
print("\n")


class Student(Person):
    def info(self):
        print(self.age)


stu = Student()
# print(stu.__name )
print(stu.age)
stu.info()
# print(Person.hobby)
# print(Student.hobby)
# print(stu.hobby)
print(stu)
print("\n")


rs.change_value()
# Person.change_value()
print(rs)
print("\n")


class Person(object):
    __age = 18

    def get_age(self):
        # 返回私有类属性
        return Person.__age

    def set_age(self, age):
        # 修改私有类属性
        Person.__age = age


rs = Person()
print(rs.get_age())
rs.set_age(20)
print(rs.get_age())
print("\n")


class A(object):
    def __myname(self):
        print("xiaoming")

    def myname(self):
        print("xiaoming")


a = A()
a.myname()
# a.__myname()
print("\n")


class Animal:
    def __eat(self):
        print("吃东西")

    def run(self):
        self.__eat()
        print("飞快的跑")


class Bird(Animal):
    pass


b = Bird()
# b.eat()
b.run()
print("\n")


# 后单下划线避免属性与关键字名字冲突


class Person:
    def __init__(self):
        self.__age = 18

    # 访问私有实例属性
    def get_age(self):
        return self.__age

    # 修改私有实例属性
    def set_age(self, age):
        if age < 0:
            print("年龄不能小于0")
        else:
            self.__age = age

    # 定义一个类属性，通过直接访问属性的形式访问私有属性
    age = property(get_age, set_age)


p = Person()
print(p.age)
p.age = 29
print(p.age)
p.age = -1
print("\n")

print(p.get_age())
p.set_age(21)
print(p.get_age())
print("\n")


class Person:
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0:
            print("年龄不能大于0")
        else:
            self.__age = age


xiaoming = Person()
xiaoming.age = 15
print(xiaoming.age)
print("\n")


class Animal:
    def __init__(self):
        self.color = "red"


tigger = Animal()
print(tigger.color)
print("\n")


try:
    # 要捕获的代码
    # l = [1, 2, 3]
    # print(l[5])
    # print(c)
    print(9 / 0)

except NameError as msg:
    print(msg)

except IndexError as msg:
    print(msg)

except ZeroDivisionError as msg:
    print(msg)

print("hahah")
print("ranshen")
print("\n")


try:
    # print(2 / 0)
    # print(dfd)
    l = [2, 3, 4, 5, 6]
    print(l[9])
except Exception as result:
    print(result)
print("\n")


def a(s):
    return 10 / int(s)


def b(s):
    return a(s) ** 2


def main():
    try:
        b("0")
    except Exception as result:
        print(result)


main()
print("\n")


try:
    print(我是没有错误产生的)
except SyntaxError as msg:
    print(msg)
except Exception as result:
    print(result)
else:
    print("没毛病")
print("\n")


try:
    int("23")
    print("aaa.txt")
    open("aaa".txt)
    open("aaa.txt")
except Exception as result:
    print(result)
finally:
    print("不管对错我都执行")
print("\n")


# class Long(Exception):
#     def __init__(self, length):
#         self.length = length

#     def __str__(self):
#         return f"您输入的长度是{self.length},超出长度了"


# def name():
#     try:
#         name = input("请输入姓名")
#         if len(name) > 3:
#             raise Long(len(name))
#         else:
#             print(name)
#     except Long as msg:
#         print(msg)
#     finally:
#         print("执行完毕")


# name()


# class Something(Exception):
#     def __str__(self):
#         return "[Error:]请输入大于0的数字"

#     try:
#         num = int(input("请输入数字: "))
#         if num < 0:
#             raise Something
#     except Something() as msg:
#         print(msg)
#     else:
#         print("没有异常")


# print(Something)


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat = Animal("小白", 5)
cat.color = "白色"
print(cat.color)
print("\n")


import types

# 定义要添加的方法
def dynamic(self):
    print(f"{self.name}的体重是{self.weight}kg, 在{Student.school}读大学.")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}今年{self.age}岁了."


rs = Student("冉申", 20)
rs.weight = 60
rs.info = types.MethodType(dynamic, rs)
print(rs)
print(rs.weight)
xp = Student("徐鹏", 90)
Student.weight = 30
xp.info = types.MethodType(dynamic, xp)
# print(xp.weight)
print("---给类对象添加属性----")
Student.school = "北京大学"
print(xp.school)
print(rs.school)
rs.info()
xp.info()
print("\n")


class Animal:
    pass


# 定义一个类方法
@classmethod
def eat(cls):
    print("吃东西")


# 定义一个静态方法
@staticmethod
def drink():
    print("喝水")


Animal.eat = eat
Animal.eat()

Animal.drink = drink
Animal.drink()
print("\n")


class A:
    __slots__ = "name", "age"


a = A()
a.name = "旺财"
a.age = 5
print(a.name)
print(a.age)
# a.hobby = "read"
print("\n")


class Student:
    # 限制要添加的实例属性
    # __slots__速度更快
    __slots__ = "name", "age", "score"

    def __str__(self):
        return f"{self.name}年纪{self.age}"


rs = Student()
rs.name = "ranshen"
rs.age = 19
rs.score = 100
print(rs)
# 所有可引用的属性都在这里存储，不足的地方在于占用内存空间大
# print(rs.__dict__)
print("\n")


# 子类未声明__slots__时，是不会继承父类__slots__属性的
class SubStudent(Student):
    # 子类声明__slots__时，继承父类__slots__,子类的__slots__范围是父类__slots__加自身
    __slots__ = ("sex", "major")


cyy = SubStudent()
cyy.sex = "female"
cyy.major = "computer science"
cyy.name = "cyyyy"
print(cyy.sex, cyy.major, cyy.name)
print("\n")


# 私有化方法与私有化属性在子类中不能继承❕


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"{self.__name}的年龄是{self.__age}."

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age > 120 or age < 0:
            print("范围0-120")
        else:
            self.__age = age


print("\n")
