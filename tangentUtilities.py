#
#  Author: David Henry  https://github.com/mgaman
#
#  This library uses its own generic types of Point, Line, Circle, Rectangle and rightTriangle
#
#  Use my svgTangent library to interface to svgwrite
#
from enum import Enum
import math
from math import sin,cos,tan,acos,asin,atan

zero_check = 0.0001   # needed for checking equivalences or zero between floats

class buildDirection(Enum):
    clockwise = 2
    anticlockwise = 3
class smallCirclePlacement(Enum):
    LeftSameY = 0
    RightSameY = 1
    AboveSameX = 2
    BelowSameX = 3
    LeftAbove = 4
    LeftBelow = 5
    RightAbove = 6
    RightBelow = 7
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
#   Given the starting point of a line, its angle to the X axis (radian) and length
#   Calculate the end point
#
class Point:
    def __init__(self,x,y):
	# parameters must be integer or float
        if isinstance(x,(int,float)) and isinstance(y,(int,float)):
            self.x = x
            self.y = y
        else:
            print('Point values must be integer or float')
def completeLine(start: Point,angle,len):  # radians
    angle = angle % (math.pi*2)   # if angle > 360
    op = len * sin(angle)
    ad = len * cos(angle)
    return Point(start.x + ad, start.y + op)
class Line:
    def __init__(self,begin,end):
    # parameters must be points
        if isinstance(begin,Point) and isinstance(end,Point):
            self.begin = begin
            self.end = end
            self.length = math.sqrt((self.end.y - self.begin.y)**2 + (self.end.x - self.begin.x)**2)
            opposite = self.end.y - self.begin.y
            adjacent = self.end.x - self.begin.x
            if math.fabs(opposite) < 0.0001:  # line is horizontal   cannot check for == 0
                if self.begin.x < self.end.x: # extends to the right
                    an0 = math.radians(0)
                else:
                    an0 = math.radians(180)
            elif math.fabs(adjacent) < 0.0001:  # line is vertical
                if self.begin.y < self.end.y: # extends upwards
                    an0 = math.radians(90)
                else:
                    an0 = math.radians(270)
            elif self.begin.x < self.end.x:  # extends to the right
                an0 = math.atan(abs(opposite)/abs(adjacent))
                if self.begin.y < self.end.y: # and up (0-90 degrees)
                    pass  # same an0
                else:                                 # and down 270 to 360 
                    an0 = 360 - math.degrees(an0)
                    an0 = math.radians(an0)
            elif self.begin.y < self.end.y:   # extends to the left and up 90 to 180
                an0 = math.atan(abs(opposite)/abs(adjacent))
                an0 = math.radians(180) - an0
            else:                                     # extends to the left and down 180 to 270
                an0 = math.atan(abs(opposite)/abs(adjacent))
                an0 = math.radians(180) + an0
            self.slope =an0
        else:
            print('Line values must be 2 points')
    def reverse(self):  # swap begin, end and reavaluate slope
        temp = self.begin
        self.begin = self.end
        self.end = temp
        self.slope = self.slope + math.radians(180)
        return self
class Circle:
    def __init__(self,c,r):
    # parameters must be numeric and a point
        if isinstance(r,(int,float)) and isinstance(c,Point):
            self.radius = r
            self.center = c
        else:
            print ('Circle values must be a number and a point')
class Rectangle:
    def __init__(self,line0: Line,line1length,direction:buildDirection ):  # line0,line1 always perpendicular
        self.sides = [line0]
        self.side1length = line1length
        if direction == buildDirection.clockwise:
            self.angleIncrement = -math.radians(90)
        else:
            self.angleIncrement = math.radians(90)
    # given the initial data, calculate the remaining lines and corners
#    def complete(self):
        # length irrespective of orientation of the line however angle of slope (an0) is
        side0length = self.sides[0].length
        an0 = self.sides[0].slope
        # calculate 2nd line
        ann = an0 + self.angleIncrement
        pt = completeLine(self.sides[0].end,ann,self.side1length)
        self.sides.append(Line(self.sides[0].end,pt))
        # calculate 3rd line
        ann = ann + self.angleIncrement
        pt = completeLine(self.sides[1].end,ann,side0length)
        self.sides.append(Line(self.sides[1].end,pt))
        # calculate 4th line (redundant really)
        ann = ann + self.angleIncrement
        pt = completeLine(self.sides[2].end,ann,self.side1length)
        self.sides.append(Line(self.sides[2].end,pt))
    def toString(self):
        strs = []
        for i in range(len(self.sides)):
            strs.append('Line '+ str(i)+': begin x '+'{:.4f}'.format(self.sides[i].begin.x)+',y '+'{:.4f}'.format(self.sides[i].begin.y)+' end x '+"{:.4f}".format(self.sides[i].end.x)+',y '+"{:.4f}".format(self.sides[i].end.y))
            strs.append('>>> length '+'{:.4f}'.format(self.sides[i].length)+' slope '+'{:.4f}'.format(math.degrees(self.sides[i].slope)))
        return strs
#
#  Construct a right angled triangle from its parts
#  If we know 1 complete line definition and length of 2nd line, all the rest can be calculated
class rightTriangle:
    def __init__(self,**args):
        self.properties = args    # make a dictionary of given properties
        if 'hypoteneuse' in self.properties:
            if 'oppositeLength' in self.properties:
                adjacentLength = math.sqrt(self.properties['hypoteneuse'].length**2 - self.properties['oppositeLength']**2)
                a1 = math.atan(self.properties['oppositeLength']/adjacentLength)  # angle opposite 'opposite'
                if self.properties['direction'] == buildDirection.clockwise:
                    a1 = -a1
                # calculate adjacent line
                pt = completeLine(self.properties['hypoteneuse'].begin,a1+self.properties['hypoteneuse'].slope,adjacentLength)
                self.properties['adjacent'] = Line(self.properties['hypoteneuse'].begin,pt).reverse()  # keep lines in same direction
                # complete opposite line
                self.properties['opposite'] = Line(self.properties['hypoteneuse'].end,self.properties['adjacent'].begin)
    def toString(self):
        ss =  'hypoteneuse begin x:'+'{:.4f}'.format(self.properties['hypoteneuse'].begin.x)+' y:'+'{:.4f}'.format(self.properties['hypoteneuse'].begin.y)
        ss = ss + ' end x:'+'{:.4f}'.format(self.properties['hypoteneuse'].end.x)+' y:'+'{:.4f}'.format(self.properties['hypoteneuse'].end.y)
        ss = ss + ' length '+'{:.4f}'.format(self.properties['hypoteneuse'].length)
        ss = ss + ' theta '+'{:.4f}'.format(math.degrees(self.properties['theta']))
        return ss
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
#  given 2 circles (1st argument smaller circle)
#  return their respective placement
#
def getPlacement(csmall: Circle,cbig: Circle):
    if csmall.center.x == cbig.center.x:   # same X, check y
        if csmall.center.y > cbig.center.y:
            csPlace = smallCirclePlacement.AboveSameX
        else:
            csPlace = smallCirclePlacement.BelowSameX
    elif csmall.center.y == cbig.center.y: # same Y check x
        if csmall.center.x < cbig.center.x:
            csPlace = smallCirclePlacement.LeftSameY
        else:
            csPlace = smallCirclePlacement.RightSameY
    elif csmall.center.x < cbig.center.x:  # small to left
        if csmall.center.y > cbig.center.y:
            csPlace = smallCirclePlacement.LeftAbove
        else:
            csPlace = smallCirclePlacement.LeftBelow
    elif csmall.center.y > cbig.center.y:  # small to right
            csPlace = smallCirclePlacement.RightAbove
    else:
        csPlace = smallCirclePlacement.RightBelow
    return csPlace
#
#  Examine circles to determine solution strategy
#  No sanity checks done to see if solution possible
# 
def Tangents(ca : Circle,cb : Circle,solution=tangentType.External):
    global zero_check
    if abs(ca.radius - cb.radius) < zero_check:
#    if ca.radius == cb.radius:
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
    #
    # We are working on the quadrangle defined by the 2 circle centers and the contact points of the tangent
    # There are 2 quadrangles, one to each tangent
    #
    # For the divergent solution we divide the quadrangle into a rectangle and a triangle
    # This is not necessary for parallel as they are essentially the same thing
    #

    # H1 is the line joining the centers
    centerSmall=Point(csmall.center.x,csmall.center.y)
    centerBig=Point(cbig.center.x,cbig.center.y)
    H1 = Line(centerSmall,centerBig)
    if solType == tangentShape.divergent:
        # 1st triangle csmall center to cbig radius in anticlockwise direction
        tr1 = rightTriangle(hypoteneuse=H1,oppositeLength=cbig.radius - csmall.radius,direction=buildDirection.anticlockwise)
        # now make rectangle from adjacent
        rc1 = Rectangle(tr1.properties['adjacent'].reverse(),csmall.radius,buildDirection.anticlockwise)
        # repeat for the other side
        tr2 = rightTriangle(hypoteneuse=H1,oppositeLength=cbig.radius - csmall.radius,direction=buildDirection.clockwise)
        rc2 = Rectangle(tr2.properties['adjacent'].reverse(),csmall.radius,buildDirection.clockwise)
    else:
        rc1 = Rectangle(H1,csmall.radius,buildDirection.anticlockwise)
        rc2 = Rectangle(H1,csmall.radius,buildDirection.clockwise)
    #rc1.complete()
    #rc2.complete()
    # tangent is third line of rectangle
    return [rc1.sides[2],rc2.sides[2]]
def setZeroCheck(f):
    global zero_check
    zero_check = f
  
