class Point(object):
    """Represents a point in 2-D Cartesian space.
    """


    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = x


    def __str__(self):
        return("(%g , %g)" % (self.x, self.y))


p = Point()

print(p)

p.x = 123.4245
p.y = 42


print(p)
