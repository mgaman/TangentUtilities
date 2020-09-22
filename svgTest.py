import svgwrite
from svgTangent import svgTangents

def testSVGLeft():
    # left below  OK
#    dwg = svgwrite.Drawing('leftbelow.svg')
#    csmall=dwg.circle([1,1],1,fill='none',stroke='blue',stroke_width=.1) 
#    cbig=dwg.circle([10,10],6,fill='none',stroke='red',stroke_width=.1)
#    ls = svgTangents(csmall,cbig)
    # left same y OK
#    dwg = svgwrite.Drawing('leftsamey.svg')
#    csmall=dwg.circle([1,10],1,fill='none',stroke='blue',stroke_width=.1) 
#    cbig=dwg.circle([9,10],6,fill='none',stroke='red',stroke_width=.1)
#    ls = svgTangents(csmall,cbig)
    # left same y OK
    dwg = svgwrite.Drawing('leftabove.svg')
    csmall=dwg.circle([1,10],1,fill='none',stroke='blue',stroke_width=.1) 
    cbig=dwg.circle([9,9],6,fill='none',stroke='red',stroke_width=.1)
    ls = svgTangents(csmall,cbig)
    # add to drawing
    dwg.add(csmall)
    dwg.add(cbig)
    dwg.add(ls[0])
    dwg.add(ls[1])
    dwg.save() 
