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

print(X.data1, X.__dict__["data1"])
X.data3 = "toast"
print(X.__dict__)
X.__dict__["data3"] = "ham"
print(X.data3)
print("\n")


# docstring
import docstr

print(docstr.__doc__)
print(docstr.func.__doc__)
print("\n")

print(docstr.spam.__doc__)
print(docstr.spam.method.__doc__)
print("\n")

x = docstr.spam()
x.method()
print("\n")


help(docstr)
