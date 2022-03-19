def countlines(file):
    file.seek(0)
    return len(file.readlines())


def countchars(file):
    file.seek(0)
    return len(file.read())


def test(name):
    file = open(name)
    return countlines(file), countchars(file)
