def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)
    return

#countdown(10)


def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)


print_n(5, 6)

