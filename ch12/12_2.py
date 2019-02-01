import random



def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    result = []

    for (length, word) in t:
        result.append(word)

    return result

def unstable_sort(words):
    t = []

    for word in words:
        t.append((len(word), random.random(), word))


    t.sort(reverse = True)

    result = []
    
    for (length, rand, word) in t:
        result.append(word)

    return result







sent = "The quick brown fox jumps over the lazy dog aa bb cderfg this is a word all work and no play makes jack a dull boy"

words = sent.split()

#words = ['a', 'aa', 'aaa', 'aaaa', 'b', 'bb', 'bbb', 'zzzz']

print(sort_by_length(words))
print(unstable_sort(words))
