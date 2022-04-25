class Animal:
    def __init__(self, name):
        self.name = name
        print("__init__方法被调用")
        # 析构方法，当对象被销毁，python解释器会自动调用

    def __del__(self):
        print("__del__对象被调用")
        print(f"{self.name}对象被销毁")


dog = Animal("旺财")
print("\n")


class Animal:
    def __init__(self, name):
        self.name = name
        print("这是构造初始化方法")

    def __del__(self):
        print("这是析构方法")


cat = Animal("才才")
