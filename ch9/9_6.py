
def is_abecedarian(word):
    
    index = word[0]
    
    for letter in word:
        if letter < index:
            return False
        index = letter

    return True



fin = open("words.txt")



wordlist = [] 

for line in fin:
    word = line.strip()

    if is_abecedarian(word):
        wordlist.append(word)
print(wordlist)
print(len(wordlist))


