
def gcd(a, b):
    print("GCD of ", a, "and", b, "is: \n")
    if b == 0:
        result = a

    else:
        result = gcd(b, a%b)
    return result



print(gcd(4, 2))
print(gcd(5, 2))
print(gcd(9, 6))
print(gcd(27, 20))
print(gcd(49, 35))
print(gcd(35, 49))
