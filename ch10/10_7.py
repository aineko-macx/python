def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    else:
        t1 = list(word1)
        t2 = list(word2)
        t1.sort()
        t2.sort()
        if t1 == t2:
            return True
        else:
            return False



print(is_anagram("abcdefg", "abcdefg"))
print(is_anagram("12334", "43213"))
print(is_anagram("adbf", "cdfgee"))
print(is_anagram("1a2b3c4d", "b4321acd"))
print(is_anagram("1234", "abcd"))
