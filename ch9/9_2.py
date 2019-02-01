def has_no_e(word):
    
    if 'e' in word:
        return False
    else:
        return True

fin = open("words.txt")
Sans_e = []
e = []
for line in fin:
    word = line.strip()

    if has_no_e(word):
        print(word)
        Sans_e.append(word)
    else:
        e.append(word)


contains_e = len(e)
e_less = len(Sans_e)

percent = e_less / (contains_e+e_less)

print(percent*100, "%")
