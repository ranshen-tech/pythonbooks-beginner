# 3.7
print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print("\n")


# 5.5
for item in range(10):
    if item == 3:
        break
    print(item)
else:
    print("for over!")
print("\n")


i, r, s, t = 100, 0, 0, 0
while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == r**3 + s**3 + t**3:
        print("i =", str(i))
    i += 1
print("\n")


for i in range(100, 1000):
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == r**3 + s**3 + t**3:
        print("i =", str(i))
print("\n")


# 6.1
a = "Hello"
print(max(a))
print(min(a))
print(len(a))
print(a[::-1])
print("\n")


# 6.2
print(list("hello"))
list = [20, 10, 50, 30]
t = [1, 2, 3]
list.extend(t)
print(list)
list.insert(2, 80)
print(list)
print("\n")


# 6.3
print(tuple([21, 23, 32, 43]))
print("\n")


# 6.4
a = set("hello")
print(a)
print(type(a))
b = {}
print(type(b))
print("\n")


# 6.6
d = {1: "ran", 2: "xu", 3: "zhu"}
print("---遍历键---")
for k in d.keys():
    print(f"学号: {k}")

print("\n---遍历值---")
for v in d.values():
    print(f"学生: {v}")

print("\n---遍历键:值---")
for d_id, d_name in d.items():
    print(f"学号: {d_id} - 学生: {d_name}")
print("\n")


# 7.4
s = "hello world"
print(s.find("l", 4, 10))
print("\n")


wordstring = """
    it was the best of time it was the worst of time.
    it was the wisdom of age it was the foolish of age.
    """
# 标点符号替换
wordstring = wordstring.replace(".", "")
print(wordstring)

# 分割单词
wordlist = wordstring.split()
print(wordlist)

wordreq = []
for w in wordlist:
    # 统计单词出现个数
    wordreq.append(wordlist.count(w))

d = dict(zip(wordlist, wordreq))
print(d)
print("\n")


s = "Python"
print("{}".format(s))
print("\n")


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


# class Dog:
#     # 构造方法
#     def __init__(self, name, age, sex='雌性'):
#         self.name = name # 创建和初始化实例变量name
#         self.__age = age # 创建和初始化私有化变量__age

#     # 实例方法
#     def run(self):
#         print(f'{self.name}在跑...')
