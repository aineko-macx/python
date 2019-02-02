from swampy.TurtleWorld import *
import math


def square(t, length):

    for i in range(4):
        fd(t, length)
        lt(t)
    
    return None



def polygon(t, length, n):

    exterior = 360/n
    interior = 180 - exterior

    for i in range(n):
        fd(t, length)
        lt(t, exterior)
    
    return None

def circle(t, r):


    circumference = 2*math.pi*r
    
    n = 15

    length = circumference/n


    polygon(t, length, n)

    return None

def arc(t, r, angle):
    """this is a docstring for arc"""
    circumference = 2*math.pi*r

    sides = 15*angle/360
    n = 15

    length = circumference/n

    exterior = 360/n

    for i in range(sides+1):
        fd(t, length)
        lt(t, exterior)

    return None



world = TurtleWorld()
bob = Turtle()

bob.delay = 0.01

#square(bob, 100)

#polygon(bob, 100, 8)

#circle(bob, 100)

arc(bob, 100, 180)
print arc.__doc__


wait_for_user()
