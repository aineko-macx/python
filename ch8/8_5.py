def count(s):
    count = 0
    for letter in s:
        if letter == 'a':
            count += 1
    return count


print(count('banana'))
