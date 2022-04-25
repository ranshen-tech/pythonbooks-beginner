class Person:
    # name = "shawn ran"
    age = 29

    def __init__(self):
        self.name = "ran"

    def eat(self):
        print("大口吃饭")

    def run(self):
        print("飞速的跑")


xm = Person()
xm.eat()
xm.run()
print(f"{xm.name}的年龄是: {xm.age}")
print("\n")


# 定义在类里面，方法外面的属性是类属性；定义在方法里面使用self引用的属性是实例属性
class People:
    def __init__(self):
        """实例属性的声明和初始化"""
        self.name = "Ran"
        self.sex = "男"
        self.age = 29

    def eat(self):
        print("喜欢吃苹果")


rs = People()
# 添加实例属性
rs.name = "ran"
# 添加实例属性
rs.sex = "男"
# 添加实例属性
rs.age = 29
rs.eat()
print(rs.name, rs.sex, rs.age)
print("\n")


xm = People()
print(xm.name)
xm.name = "冉"
print(xm.name)
print("\n")


class People:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def eat(self, food):
        print(f"{self.name}爱吃{food}")


rs = People("ran", "male", 29)
rs.eat("apple")
print(rs.name, rs.sex, rs.age)

xp = People("xu", "female", 14)
print(xp.name, xp.age, xp.sex)
print("\n")


class Person:
    """定义类"""

    def __init__(self, major):
        """定义专业

        Args:
            major (_type_): str
        """
        self.major = major

    def eat(self, name, food):
        """实例方法"""
        print(f"self={id(self)}")
        print(f"{name} like {food}, 专业是{self.major}")


# rs是一个新的实例话对象
rs = Person("CS")
print(f"rs={id(rs)}")
rs.eat("ran", "apple")
print(rs)
print("\n")


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print("---init函数的执行----")

    def __str__(self):
        """自定义对象的内容格式

        Returns:
            _type_: 对象内容
        """
        return f"我的名字是{self.name}, 我的颜色为{self.color}"

    def __new__(cls, *Args):
        """创建对象实例的方法 每调用一次就会生成新的对象"""
        print("new------函数的执行")
        return object.__new__(cls)


dog = Animal("旺财", "white")
print(dog)
print("\n")


class Role:
    def __init__(self, name, hp):
        """构造初始化函数"""
        self.name = name
        self.hp = hp

    def poke(self, enemy):
        enemy.hp -= 10
        info = f"{self.name}捅了{enemy.name}一刀"
        print(info)

    def chop(self, enemy):
        enemy.hp -= 15

    def cure(self):
        self.hp += 10
        info = f"{self.name}吃了一颗补血药,增加了10滴血"
        print(info)

    def __str__(self):
        return f"{self.name}还剩下{self.hp}血量"


# 创建两个实例化对象
rs = Role("冉申", 100)
xp = Role("徐鹏", 100)
# rs捅xp一刀
rs.chop(xp)
# 打印双方状态
print(rs)
print(xp)
print("*******************************")
# xp捅rs一刀
xp.poke(rs)
# 打印双方状态
print(rs)
print(xp)
print("*******************************")
# 徐鹏吃药
xp.cure()
print(rs)
print(xp)
print("\n")


rs = Role("冉申", 100)
xp = Role("徐鹏", 100)

import time

while True:
    if rs.hp <= 0 or xp.hp <= 0:
        break
    rs.chop(xp)
    # 打印双方状态
    print(rs)
    print(xp)
    print("*******************************")
    # xp捅rs一刀
    xp.poke(rs)
    # 打印双方状态
    print(rs)
    print(xp)
    print("*******************************")
    time.sleep(1)
print("对决结束.....")
print("\n")


class Student:
    def run(self):
        print("学生每天进行2000米跑步训练")


rs = Student()
rs.run()
print("\n")


class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name}的颜色是{self.color}"


apple = Fruit("apple", "red")
print(apple)
# 通过对象添加对象属性
apple.age = 13
print("*" * 40)
orange = Fruit("orange", "yellow")
print(orange)
print("*" * 40)
xigua = Fruit("西瓜", "绿皮")
print(xigua)
print("\n")


class Person:
    def weight(self):
        print(f"self的ID是{id(self)}")


liming = Person()
liming.weight()
print(id(liming))
print("\n")


class Animal:
    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}在吃东西")

    def run(self):
        print(f"{self.name}在跑")

    def __str__(self):
        return f"{self.name}的颜色是:{self.color}, {self.name}今年{self.age}岁了"


tiger = Animal("yello", "东北虎", 3)
tiger.eat()
tiger.run()
print(tiger)
