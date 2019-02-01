def do_twice(f, object):
    f(object)
    f(object)
    return


def print_spam():
    print("spam")
    return

def print_twice(string):
    print(string)
    print(string)
    return

#do_twice(print_spam)


#do_twice(print_twice, "spam")




def do_four(f, object):
    do_twice(f, object)
    do_twice(f, object)

    return


do_four(print_twice, "spam")
