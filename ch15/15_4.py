##Python 2

from swampy.World import World

class Point(object):
    """Represents a point in 2-D Cartesian space.
    """

class Rectangle(object):
    """Represents a rectangle in 2-D  Cartesian space.
    """
class Circle(object):
    """Represents a circle in 2-D Cartesian space.
    """



def draw_rectangle(canvas, Rect):
    
    x1 = Rect.corner.x
    y1 = Rect.corner.y
    x2 = x1 + Rect.width
    y2 = y1 + Rect.height
    
    bbox = [[x1,y1],[x2,y2]]

    color = Rect.color

    canvas.rectangle(bbox, outline = 'black', width = 2, fill=color)


def draw_point(canvas, Point):
    
    x1 = Point.x
    y1 = Point.y

    bbox = [[x1,y1],[x1,y1]]

    
    canvas.rectangle(bbox, outline = 'black', width = 2, fill = None)
    

def draw_circle(canvas, Circle):
    
    x1 = Circle.center.x
    y1 = Circle.center.y

    radius = Circle.radius

    canvas.circle([x1, y1], radius, outline = 'black', fill = 'red')


#Main

world = World()


myCanvas = world.ca(width = 500, height = 500, background = 'white')


myRectangle = Rectangle()
myRectangle.width = 300
myRectangle.height = 200

myRectangle.color = 'MistyRose3'
myRectangle.corner = Point()
myRectangle.corner.x = -150
myRectangle.corner.y = -100


myPoint = Point()
myPoint.x = 25
myPoint.y = 25

myCircle = Circle()
myCircle.center = Point()
myCircle.center.x = 25
myCircle.center.y = 25
myCircle.radius = 50


draw_rectangle(myCanvas, myRectangle)
draw_point(myCanvas, myPoint)
draw_circle(myCanvas, myCircle)
"""
canvas = world.ca(width = 500, height = 500, background = 'white')
bbox = [[-150,-100],[150,100]]

canvas.rectangle(bbox, outline = 'black', width = 2, fill = 'green4')
canvas.circle([-25,0], 70, outline = None, fill = 'red')
canvas.rectangle([[0,0],[0,0]], outline = 'black')
"""


world.mainloop()
