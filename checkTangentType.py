import tangentUtilities
from tangentUtilities import Line,Circle,Point,numTangents

def checkTangentTypes():
    # ca inside cb no overlay
    caCenter = Point(0,0)
    ca = Circle(caCenter,1)
    cb = Circle(caCenter,2)
    print('No overlap ' + str(numTangents(ca,cb)))

    # ca inside cb single contract
    caCenter = Point(0,0)
    ca = Circle(caCenter,1)
    cbCenter = Point(1,0)
    cb = Circle(cbCenter,2)
    print('overlap Single contact  internal ' + str(numTangents(ca,cb)))

    # ca overlap cb 2 external
    caCenter = Point(0,0)
    ca = Circle(caCenter,2)
    cbCenter = Point(1,0)
    cb = Circle(cbCenter,2)
    print('Ovferlap 2 touch ' + str(numTangents(ca,cb)))

    # ca touch cb 2 external 1 internal
    caCenter = Point(0,0)
    ca = Circle(caCenter,2)
    cbCenter = Point(4,0)
    cb = Circle(cbCenter,2)
    print('adjacent single touch external ' + str(numTangents(ca,cb)))

    # ca separate from cb
    ca = Circle(caCenter,2)
    cbCenter = Point(5,0)
    cb = Circle(cbCenter,2)
    print('Separate ' + str(numTangents(ca,cb)))
