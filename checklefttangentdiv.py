import tangentUtilities
from tangentUtilities import Line,Circle,Point,Tangents

#
#  place small circles to above left, left, below left of large
#
def checkLeftTangents():
    # above left
    print('above left')
    sRadius = 1
    sCenter = Point(5,5)
    sCircle = Circle(sCenter,sRadius)
    bCenter = Point(10,3)
    bCircle = Circle(bCenter,sRadius+2)
    lines = Tangents(sCircle,bCircle)
    print ('line 1 ' + printLine(lines[0]) + ' line 2 ' + printLine(lines[1]))
    #  left same Y
 #   print('left same y')
    sRadius = 1
    sCenter = Point(5,5)
    sCircle = Circle(sCenter,sRadius)
    bCenter = Point(10,5)
    bCircle = Circle(bCenter,sRadius+2)
 #   Tangents(sCircle,bCircle)
    # below left
 #   print('below left')
    sRadius = 1
    sCenter = Point(5,5)
    sCircle = Circle(sCenter,sRadius)
    bCenter = Point(10,10)
    bCircle = Circle(bCenter,sRadius+2)
#   Tangents(sCircle,bCircle)

def printLine(l: Line):
     return '(' + "{:.4f}".format(l.begin.x) + ',' + "{:.4f}".format(l.begin.y) +') ('+ "{:.4f}".format(l.end.x) + ',' + "{:.4f}".format(l.end.y) + ')'