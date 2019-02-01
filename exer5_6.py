from swampy.TurtleWorld import *
import math



def koch(t, n):
    """Draws a koch curve with length n.
       from thinkpython.org"""

    if n < 3:
        fd(t, n)
        return
    m = n / 3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    rt(t, 60)
    koch(t, m)

def snowflake(t, n):
    """Draws a snowflake (A triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        rt(t, 120)




world = TurtleWorld()
bob = Turtle()
bob.delay = 0


bob.x = -150
bob.y = 90
bob.redraw()


snowflake(bob, 30)


wait_for_user()
