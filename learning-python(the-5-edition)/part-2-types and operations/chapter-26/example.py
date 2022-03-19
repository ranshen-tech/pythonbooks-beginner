class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.setdata("King Arthur")
y.setdata(3.14159)


x.display()
y.display()

x.data = "New value"
x.display()

x.anothername = "spam"
print("\n")


class SecondClass(FirstClass):
    def display(self):
        print("Current value = %s" % self.data)


z = SecondClass()
z.setdata(42)
z.display()
x.display()
print("\n")


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return "[ThirdClass: %s]" % self.data

    def mul(self, other):
        self.data *= other


a = ThirdClass("abc")
print(a.data)
a.display()
print(a)
print("\n")

b = a + "xyz"
print(b.data)
b.display()
print(b)
print("\n")

a.mul(3)
print(a)
print("\n")


# simple class


class rec:
    pass


rec.name = "Bob"
rec.age = 40

print(rec.name)

x = rec()
y = rec()
print(x.name, y.name)

x.name = "Sue"
print(rec.name, x.name, y.name)
print("\n")


print(list(rec.__dict__.keys()))
print(list(name for name in rec.__dict__ if not name.startswith("__")))
print(list(x.__dict__.keys()))
print(y.__dict__.keys())
print("\n")


print(x.name, x.__dict__["name"])
print(x.age)
# print(x.__dict__["age"])
print("\n")

print(x.__class__)
# print(x.__bases__)
print("\n")


def uppername(obj):
    return obj.name.upper()


print(uppername(x))
print("\n")
