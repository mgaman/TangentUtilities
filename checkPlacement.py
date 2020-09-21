import tangentUtilities
from tangentUtilities import Line,Circle,Point,Tangents

def checkParallelPlacements():
    # same size circles
    # above same x
    print('pl above same x')
    caCenter = Point(0,0)
    cbCenter = Point(0,5)
    ca = Circle(caCenter,1)
    cb = Circle(cbCenter,1)
    Tangents(ca,cb)
    # below same x
    print('pl below same x')
    cbCenter = Point(0,-5)
    cb = Circle(cbCenter,1)
    Tangents(ca,cb)
    # left same x
    print('pl left same y')
    caCenter = Point(0,0)
    cbCenter = Point(5,0)
    ca = Circle(caCenter,1)
    cb = Circle(cbCenter,1)
    Tangents(ca,cb)
    # right same x
    print('pl right same y')
    caCenter = Point(0,0)
    cbCenter = Point(-5,0)
    ca = Circle(caCenter,1)
    cb = Circle(cbCenter,1)
    Tangents(ca,cb)
    # left  no difference left & right for parallel
    print('pl left')
    caCenter = Point(0,0)
    cbCenter = Point(-5,4)
    ca = Circle(caCenter,1)
    cb = Circle(cbCenter,1)
    Tangents(ca,cb)

def checkDivergentPlacements():
    # ca small, cb big below same x
    print('dv below same x')
    caCenter = Point(0,0)
    cbCenter = Point(0,10)
    ca = Circle(caCenter,1)
    cb = Circle(cbCenter,5)
    Tangents(ca,cb)
    # ca small, cb big above same x
    print('dv above same x')
    caCenter = Point(0,10)
    ca = Circle(caCenter,1)
    cbCenter = Point(0,0)
    cb = Circle(cbCenter,5)
    Tangents(ca,cb)
    # ca small, cb big left same y
    print('dv left same y')
    caCenter = Point(-5,0)
    ca = Circle(caCenter,1)
    cbCenter = Point(0,0)
    cb = Circle(cbCenter,5)
    Tangents(ca,cb)
    # ca small, cb big right same y
    print('dv right same y')
    caCenter = Point(0,0)
    ca = Circle(caCenter,1)
    cbCenter = Point(-5,0)
    cb = Circle(cbCenter,5)
    Tangents(ca,cb)
    # ca small, cb big left different y
    print('dv left')
    caCenter = Point(-5,0)
    ca = Circle(caCenter,1)
    cbCenter = Point(0,10)
    cb = Circle(cbCenter,5)
    Tangents(ca,cb)
    # ca small, cb big right different y
    print('dv right')
    caCenter = Point(0,0)
    ca = Circle(caCenter,1)
    cbCenter = Point(-5,10)
    cb = Circle(cbCenter,5)
    Tangents(ca,cb)
