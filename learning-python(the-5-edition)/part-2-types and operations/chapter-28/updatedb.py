import shelve

db = shelve.open("persondb")

for key in sorted(db):
    print(key, "\t=>", db[key])


sue = db["Sue Jones"]
sue.giveRaise(0.10)
db["Sue Jones"] = sue
db.close()
print("\n")


import shelve

db = shelve.open("persondb")
rec = db["Sue Jones"]
print(rec)
print(rec.lastName())
print(rec.pay)
