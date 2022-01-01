class Parent(object):

    def altered(self):
        print("Parent altered()")

class Child(Parent):

    def altered(self):
        print("Child, Before parent altered()")
        super(Child, self).altered()
        print("Child, After parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()