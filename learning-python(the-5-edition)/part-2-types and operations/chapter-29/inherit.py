class Super:
    def method(self):
        print("in Super.method")


class Sub(Super):
    def method(self):
        print("starting Sub.method")
        Super.method(self)
        print("ending Sub.method")


x = Super()
x.method()
print("\n")

x = Sub()
x.method()
print("\n")


# abstract super class
class Super:
    def delegate(self):
        self.action()

    def action(self):
        assert False, "action must be defined!"


X = Super()
# X.delegate()


class Super:
    def delegate(self):
        self.action()

    def action(self):
        raise NotImplementedError("action must be defined!")


X = Super()
# X.delegate()


class Sub(Super):
    pass


X = Sub()
# X.delegate()


class Sub(Super):
    def action(self):
        print("spam")


X = Sub()
X.delegate()
