def find(word, letter, index):
    #index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1




print(find('quintessence', 'q',0))
print(find('baseborn', 'e',1))
print(find('baseborn', 'e',4))
