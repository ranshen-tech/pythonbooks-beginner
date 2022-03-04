from inter2 import intersect, union

s1, s2, s3 = "SPAM", "SCAM", "SLAM"

print(intersect(s1, s2))
print(union(s1, s2))
print(intersect([1, 2, 3], (1, 4)))
print(intersect(s1, s2, s3))
print(union(s1, s2, s3))
print("\n")


def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace:
            print(items)
        print(sorted(func(*items)))


tester(intersect, ("a", "abcdefg", "abdst", "albmacnd"))
print("\n")
tester(union, ("a", "abcdefg", "abdst", "albmcnd"), False)
print("\n")
tester(intersect, ("ba", "abcdefg", "abdst", "albmcnd"), False)
print("\n")


print(intersect([1, 2, 1, 3], (1, 1, 4)))
print(union([1, 2, 1, 3], (1, 1, 4)))
tester(intersect, ("ababa", "abcdefga", "aaaab"), False)
print("\n")


# def tester(func, items, trace=True):
# for args in scramble(items):
# ...use args...
