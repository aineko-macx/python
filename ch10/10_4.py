def middle_pop(list):
    list.pop(0)
    list.pop()
    return list


def middle_del(list):
    del list[0]
    del list[-1]
    return list





print(middle_pop([1,2,3,4]))
print(middle_del([1,2,23,4]))
