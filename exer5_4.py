


def is_triangle(a, b, c):
    

    if a > (b+c) or b > (a+c) or c > (b+a):
        print("no")
    else:
        print("yes")
    
    return

def user_input():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    is_triangle(a, b, c)
    return


user_input()
user_input()
user_input()
