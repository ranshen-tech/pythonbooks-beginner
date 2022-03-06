# lambda expression basis

# lambda argument1, argument2, ...argumentN: expression using arguments


def func(x, y, z):
    return x + y + z


print(func(2, 3, 4))
print("\n")

f = lambda x, y, z: x + y + z
print(f(2, 3, 4))
print("\n")

x = lambda a="fee", b="fie", c="foe": a + b + c
print(x("wee"))
print(x())
print(x("ranshen", "good", "luck"))
print("\n")


def knights():
    title = "Sir"
    action = lambda x: title + " " + x
    return action


act = knights()
msg = act("robin")
print(msg)
print(act)
print("\n")
