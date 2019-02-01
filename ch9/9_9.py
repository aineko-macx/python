def get_strings():
    Strings = []
    for i in range(100):
        if len(str(i)) <2:
            Strings.append('0'+str(i))
        else:
            Strings.append(str(i))
    return Strings



print(get_strings())
