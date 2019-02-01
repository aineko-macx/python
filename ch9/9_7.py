    
def three_doubles(word):

    if len(word) < 6:
        return False

    for i in range(len(word)-6):
        if word[i] == word[i+1]:
            if word[i+2] == word[i+3]:
                if word[i+4] == word[i+5]:
                    return True
    return False
                       

fin = open("words.txt")



wordlist = [] 

for line in fin:
    word = line.strip()

    if three_doubles(word):
        wordlist.append(word)
print(wordlist)
print(len(wordlist))


