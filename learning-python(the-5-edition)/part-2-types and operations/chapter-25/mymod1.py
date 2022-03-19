def countlines(name):
    return sum(+1 for line in open(name))


def countchars(name):
    return sum(len(line) for line in open(name))


def test(name):
    return countlines(name), countchars(name)
