import tangentUtilities
from tangentUtilities import Line,Circle,Point,Tangents

def checkLines():
    pa = Point(0,0)
    pb = Point(1,1)
    la = Line(pa,pb)
    print(la)
    print(la.reverse())
    lb = Line(pb,pa)
    print(lb)
    print(lb.reverse())

def checkCircle():
    cn = Point(3,4)
    ci = Circle(cn,121.3)
    print(ci)

def checkPoint():
    p = Point(-1,1)
    print(p)