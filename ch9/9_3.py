def avoids(word, string):


    #print("Does", word, "avoid", string, "?")

    for letter in string:
        if letter in word:
            return False
    return True



fin = open("words.txt")



usrStr = input("Input string: ")
wordlist = [] 

for line in fin:
    word = line.strip()

    if avoids(word, usrStr):
        wordlist.append(word)
print(wordlist)
print(len(wordlist))


"""

print(avoids("catz", "xyz"))
print(avoids("dog", "xyzg"))
print(avoids("cat", "abct"))
print(avoids("quixotic", "xyz"))



"""
