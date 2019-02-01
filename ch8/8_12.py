
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

"""
word = "melon"
rot = -10

print(rotN(word, rot))
"""

word = input("Plaintext: ")
rot = int(input("Rotate by: "))

print(rotN(word, rot))


