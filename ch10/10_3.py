def cum_sum(list):
    sum = 0
    for element in list:
        if type(element) == int:
            sum += element
        else:
            print("Must be a list of integers")
    list[-1] = sum

    return list



print(cum_sum([1, 2, 3]))
