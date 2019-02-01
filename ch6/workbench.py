from math import pi as pi
import math


def area(radius):
    temp = pi*radius* 2
    return


#print(area(5))



def distance(x1, y1, x2, y2):
    temp1 = (x2-x1)**2
    temp2 = (y2-y1)**2
    dist = math.sqrt(temp1+temp2)

    return dist


#print(distance(1, 2, 4, 6))




def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, yp, yp))



