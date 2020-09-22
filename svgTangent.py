#
# interface between svgwrite objects and TangentUtilities
#
import svgwrite
import tangentUtilities
from tangentUtilities import Circle,Line,Point,Tangents

def svgTangents(ca,cb):  # arguments are svg shapes - Circle
    c0r = ca.__getitem__('r') # radius
    c0x = ca.__getitem__('cx')
    c0y = ca.__getitem__('cy')
    c1r = cb.__getitem__('r') # radius
    c1x = cb.__getitem__('cx')
    c1y = cb.__getitem__('cy')
    c0 = Circle(Point(c0x,c0y),c0r)
    c1 = Circle(Point(c1x,c1y),c1r)
    ls = Tangents(c0,c1)
    dwg = svgwrite.Drawing()
    b0 = [ls[0].begin.x,ls[0].begin.y]
    e0 = [ls[0].end.x,ls[0].end.y]
    ln0 = dwg.line(b0,e0,fill='none',stroke='green',stroke_width=.1)
    b1 = [ls[1].begin.x,ls[1].begin.y]
    e1 = [ls[1].end.x,ls[1].end.y]
    ln1 = dwg.line(b1,e1,fill='none',stroke='blue',stroke_width=.1)
    return [ln0,ln1]