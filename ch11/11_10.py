
def charShift(char, rot):


    if char.isupper():
        startIndex = ord('A')
    elif char.islower():
        startIndex = ord('a')
    else:
        return char

    offset = ord(char) - startIndex
    finIndex = (offset + rot)%26 + startIndex

    ciphertext = chr(finIndex)
    return ciphertext


def rotN(word, n):

    temp = ""

    for char in word:
        temp += charShift(char, n)

    return temp

def make_dict():
    fin = open("words.txt")
    d = dict()
    
    for line in fin:
        #observer that words.txt is all lower case
        word = line.strip().lower()
        d[word] = word
    return d

def rotate_pairs(word, dict):
    
    for i in range(1,14):
        
        if rotN(word, i) in dict:
            print(word, i, rotN(word, i))

dict = make_dict()

for word in dict:
    rotate_pairs(word, dict)



#word = input("Plaintext: ")
#rot = int(input("Rotate by: "))
#print(rotN(word, rot))
