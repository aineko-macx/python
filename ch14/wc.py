def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count


print(linecount('wc.py'))


print("__name__ :", __name__)
