import svgwrite
from svgTangent import *
import math
from math import cos,sin,radians


def testSVGLeft():
    # left below   OK
#    dwg = svgwrite.Drawing('leftbelow.svg')
#    csmall=dwg.circle([1,1],1,fill='none',stroke='blue',stroke_width=.1) 
#    cbig=dwg.circle([10,10],6,fill='none',stroke='red',stroke_width=.1)
    # left same y OK
    dwg = svgwrite.Drawing('leftsamey.svg')
    csmall=dwg.circle([1,10],1,fill='none',stroke='blue',stroke_width=.1) 
    cbig=dwg.circle([9,10],6,fill='none',stroke='red',stroke_width=.1)
    # left above  OK
#    dwg = svgwrite.Drawing('leftabove.svg')
#    csmall=dwg.circle([1,10],1,fill='none',stroke='blue',stroke_width=.1) 
#    cbig=dwg.circle([9,9],6,fill='none',stroke='red',stroke_width=.1)
    # add to drawing
    ls = svgTangents(csmall,cbig)
    dwg.add(csmall)
    dwg.add(cbig)
    dwg.add(ls[0])
    dwg.add(ls[1])
    dwg.save() 
def testSVGRight():
    # right below   OK
#    dwg = svgwrite.Drawing('rightbelow.svg')
#    csmall=dwg.circle([20,1],1,fill='none',stroke='blue',stroke_width=.1) 
#    cbig=dwg.circle([10,10],6,fill='none',stroke='red',stroke_width=.1)
    # right same y OK
#    dwg = svgwrite.Drawing('rightsamey.svg')
#    csmall=dwg.circle([20,10],1,fill='none',stroke='blue',stroke_width=.1) 
#    cbig=dwg.circle([9,10],6,fill='none',stroke='red',stroke_width=.1)
    # right above  OK
    dwg = svgwrite.Drawing('rightabove.svg')
    csmall=dwg.circle([20,10],1,fill='none',stroke='blue',stroke_width=.1) 
    cbig=dwg.circle([9,9],6,fill='none',stroke='red',stroke_width=.1)
    # add to drawing
    ls = svgTangents(csmall,cbig)
    dwg.add(csmall)
    dwg.add(cbig)
    dwg.add(ls[0])
    dwg.add(ls[1])
    dwg.save() 
def testSVGAboveBelow():
    # above same x
#    dwg = svgwrite.Drawing('above same x.svg')
#    csmall=dwg.circle([10,10],1,fill='none',stroke='blue',stroke_width=.1) 
#    cbig=dwg.circle([10,2],6,fill='none',stroke='red',stroke_width=.1)
    # below same x
    dwg = svgwrite.Drawing('belowsame x.svg')
    csmall=dwg.circle([10,2],1,fill='none',stroke='blue',stroke_width=.1) 
    cbig=dwg.circle([10,10],6,fill='none',stroke='red',stroke_width=.1)
    # add to drawing
    ls = svgTangents(csmall,cbig)
    dwg.add(csmall)
    dwg.add(cbig)
    dwg.add(ls[0])
    dwg.add(ls[1])
    dwg.save() 
#
#  place small in center with a ring of big at all possible solutions
def testSVGAllsmall():
    dwg = svgwrite.Drawing('allinonesmall.svg')
    # single small circle
    csmall=dwg.circle([0,0],1,fill='none',stroke='blue',stroke_width=.1) 
    dwg.add(csmall)
    hyp = 20
    for n in range(8):
        # compute position of new center of large circle
        angle = math.radians(n*45)
        x = hyp*math.sin(angle)
        y = hyp*math.cos(angle)
        cbig = cbig=dwg.circle([x,y],6,fill='none',stroke='red',stroke_width=.1) 
        dwg.add(cbig)
        ls = svgTangents(csmall,cbig)
        # decorate the tangents as you wish
        ls[0]['fill'] = 'none'
        ls[0]['stroke'] = 'green'
        ls[0]['stroke-width'] = 0.1
        ls[1]['fill'] = 'none'
        ls[1]['stroke'] = 'purple'
        ls[1]['stroke-width'] = 0.1
        dwg.add(ls[0])
        dwg.add(ls[1])
        dwg.save() 

#  place big in center with a ring of small at all possible solutions
def testSVGAllbig():
    dwg = svgwrite.Drawing('allinonebig.svg')
    # single big circle
    cbig=dwg.circle([0,0],5,fill='none',stroke='blue',stroke_width=.1) 
    dwg.add(cbig)
    hyp = 20
    for n in range(8):
        # compute position of new center of large circle
        angle = math.radians(n*45)
        x = hyp*math.sin(angle)
        y = hyp*math.cos(angle)
        csmall = dwg.circle([x,y],1,fill='none',stroke='red',stroke_width=.1) 
        dwg.add(csmall)
        ls = svgTangents(csmall,cbig)
        # decorate the tangents as you wish
        ls[0]['fill'] = 'none'
        ls[0]['stroke'] = 'orange'
        ls[0]['stroke-width'] = 0.1
        ls[1]['fill'] = 'none'
        ls[1]['stroke'] = 'purple'
        ls[1]['stroke-width'] = 0.1
        dwg.add(ls[0])
        dwg.add(ls[1])
        dwg.save() 
#
#  build a typical carburettor to inlet manifold gasket
#  A single hole in the middle for the venturi and 2 screw holes to the left and right
#  The centre of the gasket set at (0,0) with 3 holes in a straight line on the X axis.
#  Build a border around the holes at a distance of 'shoulder'.
# 
#  Note that this example uses the default dimension unit of pixels. The svgwrite macros on 'mm' or 'inch' 
#  can be used dimensions where needed e.g
#
#  from svgwrite import inch
#  venturiHole = dwg.circle([0,0],venturiRadius*inch,fill='none',stroke='blue',stroke_width=.1)
#
def gasket():
    venturiRadius = 20
    screwRadius = 5
    shoulder = 10
    screwOffset = 40
    dwg = svgwrite.Drawing('gasket.svg')
    venturiHole = dwg.circle([0,0],venturiRadius,fill='none',stroke='blue',stroke_width=.1)
    leftScrew = dwg.circle([-screwOffset,0],screwRadius,fill='none',stroke='blue',stroke_width=.1)
    righttScrew = dwg.circle([screwOffset,0],screwRadius,fill='none',stroke='blue',stroke_width=.1)
    leftShoulder = dwg.circle([-screwOffset,0],screwRadius+shoulder,fill='none',stroke='blue',stroke_width=.1)
    rightShoulder = dwg.circle([screwOffset,0],screwRadius+shoulder,fill='none',stroke='blue',stroke_width=.1)
    outerShoulder = dwg.circle([0,0],venturiRadius+shoulder,fill='none',stroke='blue',stroke_width=.1)
    # center hole
    dwg.add(venturiHole)
    # screw holes
    dwg.add(leftScrew)
    dwg.add(righttScrew)
    # left/right edges
    #dwg.add(leftShoulder)
    #dwg.add(rightShoulder)
    # top/bottom edge
    #dwg.add(outerShoulder)
    # join up the edges
    lsleft = svgTangents(leftShoulder,outerShoulder)
    # decorate the tangents as you wish
    lsleft[0]['fill'] = 'none'
    lsleft[0]['stroke'] = 'orange'
    lsleft[0]['stroke-width'] = 0.1
    lsleft[1]['fill'] = 'none'
    lsleft[1]['stroke'] = 'purple'
    lsleft[1]['stroke-width'] = 0.1
    dwg.add(lsleft[0])
    dwg.add(lsleft[1])
    # build arc from left shoulder
    p = svgArcBuild(leftShoulder,lsleft,beginFlag=False,largeFlag=False)
    p['fill'] = 'none'
    p['stroke'] = 'orange'
    p['stroke-width'] = 0.1
    dwg.add(p)
    lsright = svgTangents(rightShoulder,outerShoulder)
    # decorate the tangents as you wish
    lsright[0]['fill'] = 'none'
    lsright[0]['stroke'] = 'orange'
    lsright[0]['stroke-width'] = 0.1
    lsright[1]['fill'] = 'none'
    lsright[1]['stroke'] = 'purple'
    lsright[1]['stroke-width'] = 0.1
    dwg.add(lsright[0])
    dwg.add(lsright[1])
    # build arc from right shoulder
    p = svgArcBuild(rightShoulder,lsright,beginFlag=False,largeFlag=False)
    p['fill'] = 'none'
    p['stroke'] = 'orange'
    p['stroke-width'] = 0.1
    dwg.add(p)
    # build arc from outershoulder and top tangents
    p = svgArcBuild(outerShoulder,[lsright[0],lsleft[1]],largeFlag=False,leftFlag=False)
    p['fill'] = 'none'
    p['stroke'] = 'green'
    p['stroke-width'] = 0.2
    dwg.add(p)
    # build arc from outershoulder and bottom tangents
    p = svgArcBuild(outerShoulder,[lsright[1],lsleft[0]],largeFlag=False)
    p['fill'] = 'none'
    p['stroke'] = 'green'
    p['stroke-width'] = 0.2
    dwg.add(p)
    dwg.save()

def testParallel():
    dwg = svgwrite.Drawing('parallel.svg')
    # make slight difference in radii to see if zero_check works
    small_radius = 3
    big_radius = 3
    csmall=dwg.circle([1,10],small_radius,fill='none',stroke='blue',stroke_width=.1)
    #small_radius = small_radius + 0.00005
#    big_radius = small_radius  + 0.001
#    big_radius = small_radius  + 0.001
#    big_radius = small_radius  + 0.1
    big_radius = small_radius  - 0.5
    cbig=dwg.circle([9,10],big_radius,fill='none',stroke='red',stroke_width=.1)
    # add to drawing
    ls = svgTangents(csmall,cbig)
    # decorate the tangents as you wish
    ls[0]['fill'] = 'none'
    ls[0]['stroke'] = 'black'
    ls[0]['stroke-width'] = 0.1
    ls[1]['fill'] = 'none'
    ls[1]['stroke'] = 'black'
    ls[1]['stroke-width'] = 0.1
    dwg.add(csmall)
    dwg.add(cbig)
    dwg.add(ls[0])
    dwg.add(ls[1])
    dwg.save() 

def testOverlap():
    strokeSize = 0.1
    dwg = svgwrite.Drawing('overlap.svg')
    csmall=dwg.circle([0,0],5,fill='none',stroke='blue',stroke_width=strokeSize) 
    cbig=dwg.circle([3,3],6,fill='none',stroke='red',stroke_width=strokeSize)
    # add to drawing
    ls = svgTangents(csmall,cbig)
    # decorate the tangents as you wish
    ls[0]['fill'] = 'none'
    ls[0]['stroke'] = 'orange'
    ls[0]['stroke-width'] = strokeSize
    ls[1]['fill'] = 'none'
    ls[1]['stroke'] = 'purple'
    ls[1]['stroke-width'] = strokeSize
    dwg.add(csmall)
    dwg.add(cbig)
    dwg.add(ls[0])
    dwg.add(ls[1])
    dwg.save() 
