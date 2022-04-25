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
