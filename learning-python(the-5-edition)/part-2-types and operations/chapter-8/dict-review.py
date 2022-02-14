d = {x: x**2 for x in range(10)}
print(d)
print("\n")

d = {"spam": 2, "ham": 1, "eggs": 3}
print(list(d.values()))
print(d.values())
print(d.items())
print(list(d.items()))
print("\n")

print(d.get("spam"))
print(d.get("toast", 88))
print("\n")

d2 = {"toast": 4, "muffin": 5}
d.update(d2)
print(d)
print("\n")

table = {"holy grail": 1975, "life of brian": 1979, "the meaning of life": 1983}
print(list(table.items()))
print([title for (title, year) in table.items() if year == 1975])
print([key for key in table.keys() if table[key] == 1975])
print("\n")

d = dict.fromkeys(["a", "b", "c"], 666)
print(d)
print("\n")
