class Point(object):
    """Represents a point in 2-D Cartesian space.
    """


    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y


    def __str__(self):
        return("(%g , %g)" % (self.x, self.y))

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def __radd__(self, other):
        return self.__add__(other)


    def add_point(self, other):
        temp = Point()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp

    def add_tuple(self, tuple):
        temp = Point()
        temp.x = self.x + tuple[0]
        temp.y = self.y + tuple[1]
        return temp



p = Point()
p.x = 3
p.y= 10


print("p = ", p)

p1 = Point()
p1.x = 5
p1.y = 6

print("p1 = ", p1)
print("p + p1 = ",  p+p1)


p2 = p1+(1,1)

print("p2 = p1 + (1,1) = ", p2)

p3 = (1,1) + p2

print("p3 = (1,1) + p2 = ", p3)
