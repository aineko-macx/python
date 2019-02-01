
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


def get_strings():
    Strings = []
    for i in range(1000000):
        if len(str(i)) < 6:
            string = '0'*(6-len(str(i)))+str(i)
            Strings.append(string)
        else:
            Strings.append(str(i))
    return Strings


Strings = get_strings()

six_dig_str = [i for i in Strings if is_palindrome(i)]
six_dig_int = [(int(i)-1) for i in six_dig_str]
six_dig_str_2 = [str(i) for i in six_dig_int]



mid_four = [i for i in six_dig_str_2 if is_palindrome(i[1:-1])]
mid_four_int = [(int(i)-1) for i in mid_four]
mid_four_str = [str(i) for i in mid_four_int]

last_five = [i for i in mid_four_str if is_palindrome(i[1:])]
last_five_str = [str(int(i)-1) for i in last_five]

last_four = [i for i in last_five_str if is_palindrome(i[2:])]


print(last_four)

"""
six_dig = []
for i in range(1000000):
    if is_palindrome(str(i)):
        six_dig.append(i)


mid_four = []
for i in six_dig:
    if is_palindrome(str(i)[1:-1]):
        mid_four.append(i)

print(mid_four)
"""

