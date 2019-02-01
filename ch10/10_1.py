def nested_sum(list):
    sum = 0
    
    for i in list:
        if type(i) == type([]):
            sum += nested_sum(i)
        else:
            sum  += i
    return sum




list = [1,2,3,4,5,6]
list1 = [[1,2],3,4,[5,6]]

print(nested_sum(list))
print(nested_sum(list1))
