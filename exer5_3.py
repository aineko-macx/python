


def check_fermat(a, b, c, n):

    if n <= 2:
        print("n <=2")
    elif a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesnt work.")

    return

a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
n = int(input("n= "))


check_fermat(a, b, c, n)
