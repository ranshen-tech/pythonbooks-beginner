print(bool(None))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print("\n")


for item in range(10):
    if item == 3:
        break
    print(item)
else:
    print("for over!")
print("\n")


i, r, s, t = 100, 0, 0, 0
while i < 1000:
    r = i // 100
    s = (i - r * 100) // 10
    t = i - r * 100 - s * 10
    if i == r**3 + s**3 + t**3:
        print("i =", str(i))
    i += 1
print("\n")
