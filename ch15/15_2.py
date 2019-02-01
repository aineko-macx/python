import math



class Point(object):
    """Represents a point on a 2-D Cartesian plane"""



class Rectangle(object):
    """Represents a rectangle.

    attributes: width (float), height (float), corner (Point).
    """




def distance_between_points(Point1, Point2):

    x_dist = Point2.x - Point1.x
    y_dist = Point2.y - Point1.y

    dist = math.sqrt(x_dist**2 + y_dist**2)


    return dist


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0

    return p

def print_point(p):
    print("(%g, %g)" %(p.x, p.y))



def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    
    


#Main
box = Rectangle()

box.width = 100.0
box.height = 200.0


box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0



#center = find_center(box)
#print_point(center)

"""
grow_rectangle(box, 50, 100)
print(box.width)
print(box.height)
print_point(box.corner)
"""

print_point(box.corner)
move_rectangle(box, 50, 100)

print_point(box.corner)
