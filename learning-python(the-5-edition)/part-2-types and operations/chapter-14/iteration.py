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


# Complete iteration protocol

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
# print(L.__next__())
print("\n")

I = iter(L)
print(I.__next__())
print(next(I))
print(next(I))
print("\n")


# Manual iteration

L = [1, 2, 3]
for X in L:
    print(X**2, end=" ")
print("\n")

I = iter(L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print(X**2, end=" ")
print("\n")


# Other built-in type iterables

D = {"a": 1, "b": 2, "c": 3}
for key in D.keys():
    print(key, D[key])
print("\n")

I = iter(D)
print(next(I))
print(next(I))
print(next(I))
print("\n")

for key in D:
    print(key, D[key])
print("\n")

R = range(5)
print(R)
I = iter(R)
print(next(I))
print(next(I))
print(list(range(5)))
print("\n")

E = enumerate("spam")
print(E)
I = iter(E)
print(next(I))
print(next(I))
print(list(enumerate("spam")))
