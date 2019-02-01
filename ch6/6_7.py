



def is_power(a, b):
    if a == 0 or b == 0:
        return False
    elif b == 1:
        if a == 1:
            return True
        else:
            return False
    

    if a == 1 or (a/b == 1):
        temp = True
    elif a%b == 0 and a != 0:
        temp = is_power((a/b), b)
    else:
        temp = False

    return temp


print(is_power(287, 3))
print(is_power(128, 2))
