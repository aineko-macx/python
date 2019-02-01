

def factorial(n):
    if not isinstance(n, int):
        print("Only defined for INT!")
        return None
    elif n < 0:
        print("must be positive!")
        return None

    elif n == 0:
        return 1
    else:
        return n*factorial(n-1)



print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(10))
print(factorial("fred"))
print(factorial(-1))
