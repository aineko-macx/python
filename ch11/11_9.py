import random

def has_duplicates(t):
    temp = t
    temp.sort()
    for i in range(len(temp)-1):
        if temp[i] == temp[i+1]:
            return True
    else:
        return False



def has_duplicates_dict(t):
    
    d = {}
    for i in t:
        if i in d:
            return True
        d[i] = True
    return False


t = [1,2,3,4]
print(t)
print(has_duplicates(t))
print(has_duplicates_dict(t))

t = [1,2,3,4,1]
print(t)
print(has_duplicates(t))
print(has_duplicates_dict(t))

t = ["a", "c", "catdog", "d", "e", "f", "catdog"]
print(t)
print(has_duplicates(t))
print(has_duplicates_dict(t))

t = ["z", "x", "x", "a"]
print(t)
print(has_duplicates(t))
print(has_duplicates_dict(t))



"""
Julians = [random.randint(1,365) for i in [int]*23]

print(has_duplicates(Julians))
print(has_duplicates_dict(Julians))



t = [1,2,3]
print(has_duplicates_dict(t))
t.append(1)
print(has_duplicates_dict(t))
"""
