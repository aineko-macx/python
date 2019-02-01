


def square_root(a):
    x = a/3 #first guess
    epsilon = 0.00000001

    while True:
        print(x)
        y = (x + a / x) / 2
        if abs(y-x) < epsilon:
            break
        x = y

    return x




square_root(169)
