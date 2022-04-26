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
