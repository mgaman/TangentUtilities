import tangentUtilities
from tangentUtilities import *

def checkVertical():
    bg = Point(0,0)
    en = Point(0,10)
    ln0 = Line(bg,en)
    rc  = Rectangle(ln0,5,rectangleDirection.clockwise)
    strs = rc.complete()
    for s in rc.toString():
        print(s)
    rc  = Rectangle(ln0,5,rectangleDirection.anticlockwise)
    rc.complete()
    for s in rc.toString():
        print(s)

def checkHorizontal():
    bg = Point(0,0)
    en = Point(10,0)
    ln0 = Line(bg,en)
    rc  = Rectangle(ln0,5,rectangleDirection.clockwise)
    strs = rc.complete()
    for s in rc.toString():
        print(s)
    rc  = Rectangle(ln0,5,rectangleDirection.anticlockwise)
    rc.complete()
    for s in rc.toString():
        print(s)
