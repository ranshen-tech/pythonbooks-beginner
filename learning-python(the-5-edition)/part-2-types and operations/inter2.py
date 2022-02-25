def intersect(*arguments):
    requests = []
    for x in arguments[0]:
        if x in requests:
            continue
        for other in arguments[1:]:
            if x not in other:
                break
        else:
            requests.append(x)
    return requests


def union(*arguments):
    requests = []
    for sequence in arguments:
        for x in sequence:
            if not x in requests:
                requests.append(x)
    return requests
