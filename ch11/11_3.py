def print_hist(h):
    for c in h:
        print(c, h[c])

def histogram(s):
    d = dict()
    for c in s:
        temp = d.get(c, 0)
        d[c] = temp +1
    return d


def get_keys(histogram):
    t = []
    k = histogram.keys()
    for element in k:
        t.append(element)

    t.sort()

    for i in t:
        print(i, histogram[i])
    return 



h = histogram('parrot')
get_keys(h)


