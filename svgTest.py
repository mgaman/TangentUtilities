import svgwrite
from svgTangent import svgTangents

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
