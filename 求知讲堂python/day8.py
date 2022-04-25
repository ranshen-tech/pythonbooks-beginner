# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("__init__方法被调用")
#         # 析构方法，当对象被销毁，python解释器会自动调用

#     def __del__(self):
#         print("__del__对象被调用")
#         print(f"{self.name}对象被销毁")


# dog = Animal("旺财")
# print("\n")


# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("这是构造初始化方法")

#     def __del__(self):
#         print("这是析构方法")


# cat = Animal("才才")
# print("\n")


class Animal:
    def eat(self):
        print("eat")

    def drink(self):
        print("drink")


class Cat(Animal):
    def mmj(self):
        print("小猫喵喵叫")


class Dog(Animal):
    def wwj(self):
        print("小狗汪汪叫")


d1 = Dog()
d1.eat()
d1.wwj()
c1 = Cat()
c1.eat()
c1.mmj()
print("\n")


class Immortal:
    def fly(self):
        print("神仙会飞")


class Monkey:
    def eat(self):
        print("猴子喜欢吃桃")


class MonkeyKing(Immortal, Monkey):
    pass


sun = MonkeyKing()
sun.fly()
sun.eat()
print("\n")


class D(object):
    def eat(self):
        print("D.eat")


class C(D):
    def eat(self):
        print("C.eat")


class B(D):
    pass


class A(B, C):
    pass


a = A()
# 首先去A中查找，A没有则去B，B没有则去C中查找，如果C类没有则去D类查找，如果还没有则报错
# A-B-C-D
a.eat()
# 可以显示类的依次继承关系
print(A.__mro__)
print("\n")


class GrandFather:
    def eat(self):
        print("吃饭")


class Father(GrandFather):
    pass


class Son(Father):
    pass


son = Son()
son.eat()
