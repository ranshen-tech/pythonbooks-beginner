from step5 import Person, Manager

bob = Person("Bob Smith")
sue = Person("Sue Jones", job="dev", pay=100_000)
tom = Manager("Tom Jones", 50_000)

import shelve

db = shelve.open("persondb")
for obj in (bob, sue, tom):
    db[obj.name] = obj
print("\n")

print(len(db))
print(list(db.keys()))
bob = db["Bob Smith"]
print(bob)
print(bob.lastName())
print("\n")

for key in db:
    print(key, "=>", db[key])
print("\n")

for key in sorted(db):
    print(key, "=>", db[key])
db.close()
