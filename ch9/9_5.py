
def uses_all(word, string):

    for i in string:
        if i not in word:
            return False

    return True




fin = open("words.txt")



usrStr = input("Input string: ")
wordlist = [] 

for line in fin:
    word = line.strip()

    if uses_all(word, usrStr):
        wordlist.append(word)
print(wordlist)
print(len(wordlist))


