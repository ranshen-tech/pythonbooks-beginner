def intersect(*args):
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
        else:
            print(x)
            res.append(x)
    return res


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res


s1, s2, s3 = "SPAM", "SCAM", "SLAM"
intersect(s1, s2)
