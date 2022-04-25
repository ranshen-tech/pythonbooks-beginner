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
    def eat(self):
        print("爸爸经常吃海鲜")


class Son(Father):
    pass


son = Son()
print(Son.__mro__)
son.eat()
print("\n")


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("汪汪叫")


class Corgi(Dog):
    # 重写类的方法
    def __init__(self, name, color):
        # 调用父类方法
        # super()是自动找到父类然后调动方法
        super().__init__(name, color)
        self.height = 90
        self.weight = 20

    def __str__(self):
        return f"{self.name}的颜色是{self.color},它的身高是{self.height}cm,体重是{self.weight}kg."

    def bark(self):
        super().bark()
        print("叫的跟神一样")
        print(self.name)


corgi = Corgi("柯基犬", "红色")
corgi.bark()
print(corgi)
print("\n")


class Animal:
    def say(self):
        print("我是动物")


class Duck(Animal):
    def say(self):
        print("我是一只鸭子")


class Dog(Animal):
    def say(self):
        print("我是一只狗")


class Cat(Animal):
    def say(self):
        print("我是一只猫")


class Bird(Animal):
    def say(self):
        print("我是一只鸟")


class Student(Animal):
    def say(self):
        print("我是学生")


duck = Duck()
duck.say()
dog = Dog()
dog.say()
cat = Cat()
cat.say()
print("\n")


def common_invoke(obj):
    """统一调用的方法

    Args:
        obj (_type_): _description_
    """
    obj.say()


list_ojb = [Dog(), Cat(), Duck(), Bird(), Student()]
for item in list_ojb:
    common_invoke(item)
print("\n")


class F1:
    def show(self):
        return "F1.show"


class S1:
    def show(self):
        return "S1.show"


class S2:
    def show(self):
        return "S2.show"


def Func(obj):
    print(obj.show)


s1_obj = S1()
Func(s1_obj)
s2_obj = S2()
Func(s2_obj)
print("\n")


class Student:
    name = "ran"

    def __init__(self, age):
        self.age = age


rs = Student(18)
# 通过实例对象可以访问类属性
print(rs.name)
# 通过实例对象对类属性进行修改, 不可以！！！
rs.name = "shawn ran"
print(rs.name)
# 通过类对象对类属性进行修改， 可以！！！
Student.name = "Shawn Ran"
print(Student.name)
print(rs.age)
print("------通过类对象去访问name---------")
# 通过类对象访问name属性
print(Student.name)
# 类属性是可以被类对象和实例对象共同访问使用  类名.属性名
# 实例属性只能由实例对象访问
print("\n")
