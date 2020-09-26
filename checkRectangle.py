import tangentUtilities
from tangentUtilities import *

def checkVertical():
    bg = Point(0,0)
    en = Point(0,10)
    ln0 = Line(bg,en)
    rc  = Rectangle(ln0,5,rectangleDirection.clockwise)
    rc.complete()
    rc.toString()
    rc  = Rectangle(ln0,5,rectangleDirection.anticlockwise)
    rc.complete()
    rc.toString()
    