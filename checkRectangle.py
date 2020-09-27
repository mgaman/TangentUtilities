import tangentUtilities
from tangentUtilities import *

def complete(bg,en):
    ln0 = Line(bg,en)
    rc  = Rectangle(ln0,5,rectangleDirection.clockwise)
    strs = rc.complete()
    for s in rc.toString():
        print(s)
    rc  = Rectangle(ln0,5,rectangleDirection.anticlockwise)
    rc.complete()
    for s in rc.toString():
        print(s)

def checkVertical():
    bg = Point(0,0)
    en = Point(0,10)
    complete(bg,en)

def checkHorizontal():
    bg = Point(0,0)
    en = Point(10,0)
    complete(bg,en)

def check45():
    bg = Point(0,10)
    en = Point(10,0)
 #   complete(bg,en)   # 1st line point to bottom right
    bg = Point(10,0)
    en = Point(0,10)
    complete(bg,en)   # 1st line point to top left
  