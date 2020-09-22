#
#  Author: David Henry  https://github.com/mgaman
#
#  This library uses its own generic types of Point, Line and Circle
#  Use my svgTangent library to interface to svgwrite
#
from enum import Enum
import math
from math import sin,cos,tan,acos,asin,atan

class Point:
    def __init__(self,x,y):
	# parameters must be integer or float
        if isinstance(x,(int,float)) and isinstance(y,(int,float)):
            self.x = x
            self.y = y
        else:
            print('Point values must be integer or float')
class Line:
    def __init__(self,begin,end):
    # parameters must be points
        if isinstance(begin,Point) and isinstance(end,Point):
            self.begin = begin
            self.end = end
        else:
            print('Line values must be 2 points')

class Circle:
    def __init__(self,c,r):
    # parameters must be numeric and a point
        if isinstance(r,(int,float)) and isinstance(c,Point):
            self.radius = r
            self.center = c
        else:
            print ('Circle values must be a number and a point')

class smallCirclePlacement(Enum):
    ToLeftSameY = 0
    ToRightSameY = 1
    AboveSameX = 2
    BelowSameX = 3
    ToLeft = 4
    ToRight = 5
class tangentShape(Enum):
    parallel = 0
    divergent = 1
    convergent = 2
class tangentAvailable(Enum):
    noTangents = 0   # 1 circle inside the other. not touching
    single = 1       # 1 circle inside the other. touch 1 point
    twoExternalNoInternal = 2  # circles overlay, touch at 2 points
    twoExternalSingleInternal = 3 # circles adjacent, touch at 1 point
    twoExternalTwoInternal = 4 # circles adjacent, no touching
class tangentType(Enum):
    Internal = 1
    External = 2
#
#  Discover how many tangents exist between 2 circles
#  
def numTangents(ca,cb):  # ca,cb are Circle objects
    # c0 is the largest of the 2 circles
    if ca.radius >= cb.radius:
        r0 = ca.radius
        x0 = ca.center.x
        y0 = ca.center.y
        r1 = cb.radius
        x1 = cb.center.x
        y1 = cb.center.y
    else:
        r0 = cb.radius
        x0 = cb.center.x
        y0 = cb.center.y
        r1 = ca.radius
        x1 = ca.center.x
        y1 = ca.center.y
    D = math.sqrt(pow(x0-x1,2)+pow(y0-y1,2))
    if D < r0-r1:
        return tangentAvailable.noTangents
    elif D == r0-r1:
        return tangentAvailable.single
    elif D < r0+r1 and D > r0 -r1 :
        return tangentAvailable.twoExternalNoInternal
    elif D == r0+r1:
        return tangentAvailable.twoExternalSingleInternal
    elif D > r0+r1:
        return tangentAvailable.twoExternalTwoInternal

#
#  Examine circles to determine solution strategy
#  No sanity checks done to see if solution possible
# 
def Tangents(ca : Circle,cb : Circle,solution=tangentType.External):
    if ca.radius == cb.radius:
        solType = tangentShape.parallel
    else:
        solType = tangentShape.divergent
    # sums done from small circle to big circle
    if ca.radius < cb.radius:
        csmall = ca
        cbig = cb
    else:
        csmall = cb
        cbig = ca
    if csmall.center.x == cbig.center.x:   # same X, check y
        if csmall.center.y > cbig.center.y:
            csPlace = smallCirclePlacement.AboveSameX
        else:
            csPlace = smallCirclePlacement.BelowSameX
    elif csmall.center.y == cbig.center.y:
        if csmall.center.x < cbig.center.x:
            csPlace = smallCirclePlacement.ToLeftSameY
        else:
            csPlace = smallCirclePlacement.ToRightSameY
    elif csmall.center.x < cbig.center.x:
            csPlace = smallCirclePlacement.ToLeft
    else:
        csPlace = smallCirclePlacement.ToRight
    print(str(solType)+','+str(csPlace))
    if solType == tangentShape.parallel:
        print('Parallel TBD')
        return []
    else:   # divergent   
        # H1 is line joining centers, draw right angled triangle where H1 is hypoteneuse
        if csPlace == smallCirclePlacement.ToLeft or csPlace == smallCirclePlacement.ToLeftSameY:
            opposite = cbig.center.y - csmall.center.y
            adjacent = cbig.center.x - csmall.center.x
            h1 = math.sqrt(opposite**2 + adjacent**2)
            # a1 angle of hypoteneuse anticlockwise from x axis
            a1 = math.atan(abs(opposite)/abs(adjacent))
            # h2 is hypoteneuse of triangle where h1 is adjacent and opposite is on cbig radius
            h2 = math.sqrt(pow(h1,2) - pow(cbig.radius - csmall.radius,2))
            # angle a2 between h1 and h2
            a2 = math.acos(h2/h1)
            # we now know 1 point of a rectangle (csmall center), 2 sides csmall radius and H2
            # and angle of H2 (a1 ± a2)
            # calculate the other 3 corners and from there the tangent (which is the opposite 
            # side to H2
            tpoints = []
            if opposite >= 0:
                # 1st tangent
                side = completeLine(csmall.center,a1 + a2 + math.radians(90),csmall.radius)
                tpoints.append(side)
                endh2 = completeLine(csmall.center,a1 + a2 ,h2)
                side = completeLine(endh2,a1 + a2 + math.radians(90),csmall.radius)
                tpoints.append(side)
                # second tangent
                side = completeLine(csmall.center,a1 - a2 - math.radians(90),csmall.radius)
                tpoints.append(side)
                endh2 = completeLine(csmall.center,a1 - a2 ,h2)
                side = completeLine(endh2,a1 - a2 - math.radians(90),csmall.radius)
                tpoints.append(side)
            else:
                # 1st tangent
                side = completeLine(csmall.center,a1 - a2 - math.radians(90),csmall.radius)
                tpoints.append(side)
                endh2 = completeLine(csmall.center,a1 - a2 ,h2)
                side = completeLine(endh2,a1 - a2 - math.radians(90),csmall.radius)
                tpoints.append(side)
                # 2nd tangent
                side = completeLine(csmall.center,a1 - a2 + math.radians(90),csmall.radius)
                tpoints.append(side)
                endh2 = completeLine(csmall.center,a1 + a2 ,h2)
                side = completeLine(endh2,a1 - a2 - math.radians(90),csmall.radius)
                tpoints.append(side)
            return [Line(tpoints[0],tpoints[1]), Line(tpoints[2],tpoints[3])]
            
#   Given the starting point of a line, its angle to the X axis (radian) and length
#   Calculate the end point
#
def completeLine(start,angle,length):  # radians
# do sanity checks on paramaters if you are pedantic
#    print('calc on line angle '+"{:.4f}".format(math.degrees(angle)))
    op = length * sin(angle)
    ad = length * cos(angle)
    return Point(start.x + ad, start.y + op)
