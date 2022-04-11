# 9.4.1 实例变量
class Dog:
    def __init__(self, name, age):
        self.name = name  # 创建和初始化实例变量name
        self.age = age  # 创建和初始化实例变量age


d = Dog("球球", 2)
print(f"我们家狗狗名叫{d.name},{d.age}岁了。")
print("\n")


# 9.4.2 构造方法
class Dog:
    def __init__(self, name, age, sex="雌性"):
        self.name = name  # 创建和初始化实例变量name
        self.age = age  # 创建和初始化实例变量age
        self.sex = sex  # 创建和初始化实例变量sex


d1 = Dog("球球", 2)
d2 = Dog("哈哈", 1, "雄性")
d3 = Dog(name="拖布", sex="雄性", age=3)

print(f"{d1.name}: {d1.age}岁{d1.sex}")
print(f"{d2.name}: {d2.age}岁{d2.sex}")
print(f"{d3.name}: {d3.age}岁{d3.sex}")
print("\n")


# 9.4.3 实例方法
class Dog:
    # 构造方法
    def __init__(self, name, age, sex="雌性"):
        # 创建和初始化实例变量name
        self.name = name
        # 创建和初始化实例变量age
        self.age = age
        # 创建和初始化实例变量sex
        self.sex = sex

    # 实例方法
    def run(self):
        print(f"{self.name}在跑...")

    # 实例方法
    def speak(self, sound):
        print(f'{self.name}在叫, "{sound}"!')


dog = Dog("球球", 2)
dog.run()
dog.speak("汪汪汪")
print("\n")


# 9.4.4 类变量
class Account:
    # 类变量利率interest_rate
    interest_rate = 0.0568
    # 构造方法
    def __init__(self, owner, amount):
        # 创建并初始化实例变量owner
        self.owner = owner
        # 创建并初始化实例变量amount
        self.amount = amount


account = Account("Tony", 800000.0)

print(f"账户名: {account.owner}")
print(f"账户金额: {account.amount}")
print(f"利率: {Account.interest_rate}")
print("\n")


# 9.4.5 类方法
class Account:
    # 类变量利率interest_rate
    interest_rate = 0.0668
    # 构造方法
    def __init__(self, owner, amount):
        # 创建并初始化实例变量owner，定义实例变量账户名
        self.owner = owner
        # 创建并初始化实例变量amount，定义实例变量账户金额
        self.amount = amount

    # 类方法
    @classmethod
    def interest_by(cla, amt):
        return Account.interest_rate * amt


interest = Account.interest_by(12000.0)
print(f"计算利息: {interest}")
print("\n")


# 9.5.1 私有变量
class Account:
    # 类变量利率__interest_rate
    __interest_rate = 0.0568

    def __init__(self, owner, amount):
        # 创建并初始化公有实例变量owner
        self.owner = owner
        # 创建并初始化私有实例变量__amount
        self.__amount = amount

    def desc(self):
        print(f"{self.owner} 金额: {self.__amount} 利率: {Account.__interest_rate}")


account = Account("Tony", 800000.0)
account.desc()


# class Dog:
#     # 构造方法
#     def __init__(self, name, age, sex='雌性'):
#         self.name = name # 创建和初始化实例变量name
#         self.__age = age # 创建和初始化私有化变量__age

#     # 实例方法
#     def run(self):
#         print(f'{self.name}在跑...')
