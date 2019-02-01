import math


def estimate_pi():
    
    k = 0
    sum = 0
    C = 2*math.sqrt(2)/9801

    while True:
          
        top = math.factorial(4*k)*(1103+26390*k)
        bottom = (math.factorial(k)**4)*396**(4*k)
        term = C*top/bottom
        
        sum += term

        if abs(term) <= 1e-15:
            break
        k += 1

    return 1/sum

print(estimate_pi())
print(math.pi)
