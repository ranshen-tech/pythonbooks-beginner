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

for line in open("script2.py"):
    print(line.upper(), end="")
print("\n")

for line in open("script2.py").readlines():
    print(line.upper(), end="")
print("\n")

f = open("script2.py")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
print("\n💖")


# Manual iteration: iter & next

f = open("script2.py")
print(f.__next__().rstrip())
print(f.__next__().rstrip())
print("💖")

f = open("script2.py")
print(next(f).rstrip())
print(next(f).rstrip())
print("💖")


# Complete iteration agreement

L = [1, 2, 3]
I = iter(L)
print(I)
print(I.__next__())
print(I.__next__())
print(I.__next__())
print("\n")

f = open("script2.py")
print(iter(f) is f)
print(iter(f) is f.__iter__())
print(f.__next__())
print(next(f))
print("\💖")

L = [1, 2, 3]
print(iter(L) is L)
print(L.__next__())
