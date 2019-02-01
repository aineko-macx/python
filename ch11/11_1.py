import time

import random



def makedict(file):

    fin = open(file)
    myDict = {}
    
    for line in fin:
        word = line.strip()
        myDict[word] = random.randint(1,100)

    return myDict


dict = makedict("words.txt")

start_time = time.time()
if 'one' in dict:
    print("True")
else:
    print("False")


elapsed_time = time.time() - start_time
print(elapsed_time, "seconds")



from bisect import bisect_left

def in_bisect(t, value):

    i = bisect_left(t, value)
    if i != len(t) and t[i] == value:
        return True
    else:
        return False



def get_words():
    fin = open("words.txt")
    Words = []
    for line in fin:
        word = line.strip()
        Words.append(word)
    return Words


t = get_words()


start_time = time.time()
if 'one' in t:
    print("True")
else:
    print("False")
elapsed_time = time.time() - start_time


print(elapsed_time, "seconds")

