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
