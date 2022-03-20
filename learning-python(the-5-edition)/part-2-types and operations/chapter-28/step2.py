name = "Bob Smith"
print(name.split())
print(name)
print(name.split()[-1])
print("\n")

pay = 100000
pay *= 1.10
print("%.2f" % pay)
print("\n")


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay


if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])
    sue.pay *= 1.10
    print("%.2f" % sue.pay)
    print("\n")
