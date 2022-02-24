def keywordonly(a, *b, c):
    print(a, b, c)


keywordonly(1, 2, c=3)
keywordonly(a=1, c=3)
# keywordonly(1, 2, 3)
print("\n")


def keywordonly(a, *, b, c):
    print(a, b, c)


keywordonly(1, c=3, b=2)
keywordonly(c=3, b=2, a=1)
# keywordonly(1, 2, 3)
# keywordonly(1)
print("\n")


def keywordonly(a, *, b="spam", c="ham"):
    print(a, b, c)


keywordonly(1)
keywordonly(1, c=3)
keywordonly(a=1)
keywordonly(c=3, b=2, a=1)
# keywordonly(1, 2)
print("\n")


def kwonly(a, *, b, c="spam"):
    print(a, b, c)


kwonly(1, b="eggs")
# kwonly(1, c="eggs")
# kwonly(1, 2)
print("\n")


def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)


kwonly(3, c=4)
kwonly(3, c=4, b=5)
# kwonly(3)
# kwonly(1, 2, 3)
print("\n")
