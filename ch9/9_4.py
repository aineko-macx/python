
def uses_only(word, string):
    
    for letter in word:
        if letter not in string:
            return False
    return True



fin = open("words.txt")



usrStr = input("Input string: ")
wordlist = [] 

for line in fin:
    word = line.strip()

    if uses_only(word, usrStr):
        wordlist.append(word)
print(wordlist)
print(len(wordlist))


"""

print(avoids("catz", "xyz"))
print(avoids("dog", "xyzg"))
print(avoids("cat", "abct"))
print(avoids("quixotic", "xyz"))



"""
