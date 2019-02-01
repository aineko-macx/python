inputstr = input("input string: ")

def right_justify(inputstr):
    outputstr = inputstr

    while len(outputstr) < 70:
        outputstr = " " + outputstr

    return print(outputstr)


right_justify(inputstr)
