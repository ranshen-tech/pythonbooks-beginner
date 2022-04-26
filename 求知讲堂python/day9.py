class Person(object):
    # 定义一个私有化属性，属性前面加两个下划线
    __age = 18


class Person:
    hobby = "dance"

    def __init__(self):
        # 私有化之后就不能在类外部访问了
        self.__name = "冉申"
        self.age = 30

    def __str__(self):
        return f"{self.__name}的年龄是{self.age}"


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
print(Person.hobby)
print(Student.hobby)
print(stu.hobby)
