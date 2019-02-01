import random

def has_duplicates(t):
    temp = t
    temp.sort()
    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            return True
    else:
        return False



"""
print(has_duplicates([1,2,3,34,5,6]))
print(has_duplicates([1,1,2,3]))
print(has_duplicates(["a", "b", "c", "a"]))
"""



Julians = [random.randint(1,365) for i in [int]*23]

print(has_duplicates(Julians))

