def sumall(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(sumall(1))
print(sumall(1,2))
print(sumall(1,2,3,4,5,6,6,5,5,34))
