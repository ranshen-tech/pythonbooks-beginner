# Iterator

for x in [1, 2, 3, 4]:
    print(x**2, end=" ")
print("\n")

for x in (1, 2, 3, 4):
    print(x**3, end=" ")
print("\n")

for x in "spam":
    print(x * 2, end=" ")
print("\n")


# Iterative agreement: File iterator

print(open("script2.py").read())
print("💖")

f = open("script2.py")
print(f.readline().rstrip())
print(f.readline().rstrip())
print(f.readline().rstrip())
print(f.readline().rstrip())
print(f.readline().rstrip())
print(f.readline().rstrip())
print("💘")

f = open("script2.py")
print(f.__next__().strip())
print(f.__next__().strip())
print(f.__next__().strip())
print(f.__next__().strip())
print(f.__next__().strip())
# print(f.__next__().strip())
print("💖")
