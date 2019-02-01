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


def reverse_pair(t, word):
    rev = word[::-1]
    return in_bisect(t, rev)





def interlock(wordList, word):
    
    oddChar = word[1::2]
    evenChar = word[::2]

    return in_bisect(wordList, oddChar) and  in_bisect(wordList, evenChar)

def interlock_n(wordList, word):
   
    
    ones = word[::3]
    twos = word[1::3]
    threes = word[2::3]

    return in_bisect(wordList, ones) and  in_bisect(wordList, twos) and in_bisect(wordList, threes)



#Main
wordList = get_words()

print(len(wordList))
for word in wordList:
    if interlock_n(wordList, word):
        print(word, ":", word[::3], "&", word[1::3], "&", word[2::3])



