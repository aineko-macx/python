def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram1(s):
    d = dict()
    for c in s:
        temp = d.get(c, 0)
        d[c] = temp +1
    return d



print(histogram("abcdefg"))
print(histogram("parrot"))
print(histogram1("abcdefg"))
print(histogram1("parrot"))
