# 命名空间字典


class Super:
    def hello(self):
        self.data1 = "spam"


class Sub(Super):
    def hola(self):
        self.data2 = "eggs"


X = Sub()
print(X.__dict__)
print(X.__class__)
print(Sub.__base__)
print(Super.__bases__)
print("\n")

Y = Sub()
X.hello()
print(X.__dict__)
print("\n")

X.hola()
print(X.__dict__)
print("\n")

print(list(Sub.__dict__.keys()))
print(list(Super.__dict__.keys()))
print(Y.__dict__)
print("\n")
