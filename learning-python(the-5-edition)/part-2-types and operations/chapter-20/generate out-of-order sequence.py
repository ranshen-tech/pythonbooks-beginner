# out-of-order sequence

L, S = [1, 2, 3], "spam"
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=" ")
print("\n")


for i in range(len(L)):
    L = L[1:] + L[:1]
    print(L, end=" ")
print("\n")


for i in range(len(S)):
    X = S[i:] + S[:i]
    print(X, end=" ")
print("\n")


# simple function


def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res


print(scramble("spam"))
print("\n")


def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]


print(scramble("spam"))
print("\n")


print(scramble((1, 2, 3)))

for x in scramble((1, 2, 3)):
    print(x, end=" ")
print("\n")


# generator function


def scramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        yield seq


print(list(scramble("spam")))
print(list(scramble((1, 2, 3))))
for x in scramble((1, 2, 3)):
    print(x, end=" ")
print("\n")


def scramble(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]


print(list(scramble("spam")))
print(list(scramble((1, 2, 3))))
for x in scramble((1, 2, 3)):
    print(x, end=" ")
print("\n")


# generator expression

print(S)
G = (S[i:] + S[:i] for i in range(len(S)))
print(list(G))
print("\n")


F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(F(S))
print(list(F(S)))
print(list(F([1, 2, 3])))
print("\n")

for x in F((1, 2, 3)):
    print(x, end=" ")
print("\n")


# Test client
# from scramble import scramble

# from inter2 import intersect, union


# def tester(func, items, trace=True):
#     for args in scramble(items):
#         if trace:
#             print(args)
#         print(sorted(func(*args)))


# tester(intersect, ("aab", "abcde", "ababab"))
# tester(intersect, ([1, 2], [2, 3, 4], [1, 6, 2, 7, 3]), False)


# 全排列，所有可能的组合

from scramble import scramble, scramble2
from permute import permute1, permute2

print(list(scramble("abc")))
print("\n")

print(permute1("abc"))
print(list(permute2("abc")))
print("\n")

G = permute2("abc")
print(next(G))
print(next(G))
for x in permute2("abc"):
    print(x)
print("\n")


print(permute1("spam") == list(permute2("spam")))
print(len(list(permute2("spam"))))
print(len(list(scramble("spam"))))
print("\n")

print(list(scramble("spam")))
print(list(permute2("spam")))
