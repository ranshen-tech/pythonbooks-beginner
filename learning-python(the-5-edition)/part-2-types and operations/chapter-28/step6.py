from step5 import Person

bob = Person("Bob Smith")
print(bob)
print(bob.__class__)
print(bob.__class__.__name__)
print("\n")

print(list(bob.__dict__.keys()))
for key in bob.__dict__:
    print(key, "=>", bob.__dict__[key])
print("\n")

for key in bob.__dict__:
    print(key, "=>", getattr(bob, key))
print("\n")


print(bob.__dict__.keys())
print(dir(bob))
print(list(bob.__dict__.keys()))
print("\n")

print(len(dir(bob)))
print(list(name for name in dir(bob) if not name.startswith("__")))
