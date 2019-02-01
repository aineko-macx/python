import math

def square_root(a):
    x = a/3 #first guess                                                                            
    epsilon = 0.00000001

    while True:
        #print(x)
        y = (x + a / x) / 2
        if abs(y-x) < epsilon:
            break
        x = y

    return x




def test_square_root(a):
    col2 = square_root(a)
    col3 = math.sqrt(a)
    epsilon = col3-col2
    print(a, col2, col3, epsilon)


test_square_root(1)
test_square_root(2)
    
