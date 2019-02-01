


def is_between(x, y, z):
    if (x <= y) and (y <= z):
        return True
    else:
        return False



print(is_between(1, 2, 3))

print(is_between(1, 0, 3))
print(is_between(1, 4, 3))
