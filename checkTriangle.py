import tangentUtilities
from tangentUtilities import *

def checkTriangles():
    ca = Point(0,0)
    cb = Point(4,0)
    ad = Line(ca,cb)
    rt = rightTriangle(adjacent=ad,oppositeLength=4,direction=buildDirection.anticlockwise)
    print(rt)
    rt = rightTriangle(adjacent=ad,oppositeLength=4,direction=buildDirection.clockwise)
    print(rt)
