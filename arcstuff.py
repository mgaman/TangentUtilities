#
#  In this example we build 2 tangents between 2 circles
#  Instead of adding the circles to the file we create an arc based upon
#  each circle and the place of contact between the circle and tangents
import svgwrite
from svgTangent import *
import math
from math import cos,sin,radians


leftRadius = 1
rightRadius=6
dwg = svgwrite.Drawing('arc.svg')
cleft=dwg.circle([1,1],leftRadius,fill='none',stroke='blue',stroke_width=.1) 
cright=dwg.circle([10,10],rightRadius,fill='none',stroke='black',stroke_width=.1)
ls = svgTangents(cleft,cright)
# decorate the tangents as you wish
ls[0]['fill'] = 'none'
ls[0]['stroke'] = 'green'
ls[0]['stroke-width'] = 0.1
ls[1]['fill'] = 'none'
ls[1]['stroke'] = 'purple'
ls[1]['stroke-width'] = 0.1
p = svgArcBuild(cleft,ls,beginFlag=False,largeFlag=False)
p['fill']='none'
p['stroke'] = 'blue'
p['stroke-width'] = 0.1
#print(p.tostring())
dwg.add(p)
p = svgArcBuild(cright,ls,leftFlag=False)
p['fill']='none'
p['stroke'] = 'red'
p['stroke-width'] = 0.1
#print(p.tostring())
dwg.add(p)
dwg.add(ls[0])
dwg.add(ls[1])
dwg.save()
