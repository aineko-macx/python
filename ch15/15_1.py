import math



class Point(object):
    """Represents a point on a 2-D Cartesian plane"""





PointA = Point()

PointA.x = 1
PointA.y = 0


PointB = Point()

PointB.x = 5
PointB.y = 0




def distance_between_points(Point1, Point2):

    x_dist = Point2.x - Point1.x
    y_dist = Point2.y - Point1.y

    dist = math.sqrt(x_dist**2 + y_dist**2)


    return dist



print(distance_between_points(PointA, PointB))
