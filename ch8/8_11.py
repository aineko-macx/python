def any_lowercase1(s):
    #This function works but cannot handle exceptions
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    #Evaluates the char 'c'; output is always true
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    #Only evaluates last character
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):

    #Returns False or True if c is lowercase
    flag = False

    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):

    #Returns True for all uppercase; false if any lowercase
    for c in s:
        if not c.islower():
            return False
    return True


#print(any_lowercase1("lOWERCASE"))
#print(any_lowercase1("TItlecaDe"))



#print(any_lowercase2("lowercase"))
#print(any_lowercase2("TITTIES"))


#print(any_lowercase3("lowercase"))
#print(any_lowercase3("camelCasE"))


#print(any_lowercase4("lowercase"))
#print(any_lowercase4("UPPERCASE"))


print(any_lowercase5("lowercase"))
print(any_lowercase5("UP"))


