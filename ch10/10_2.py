def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def capitalize_nested(list):
    result = []
    

    for element in list:
        if type(element) == type([]):
            result.append(capitalize_nested(element))
        else:
            result.append(element.capitalize())
    return result



print(capitalize_nested(['a', 'b', 'c', 'd']))

print(capitalize_nested([['a', ['b','c']], 'b', 'c', ['d', 'e','f']]))
