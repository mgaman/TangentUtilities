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
    ln0 = dwg.line(b0,e0)
    b1 = [ls[1].begin.x,ls[1].begin.y]
    e1 = [ls[1].end.x,ls[1].end.y]
    ln1 = dwg.line(b1,e1)
    return [ln0,ln1]

#
#  Build an arc based upon the interection of a circle and 2 tangents
#
#  beginFlag - take begining of line, else take the end
#  largeFlag - large arc else small arc
#  leftFlag -  build to the left, else right
def svgArcBuild(circle,lines,beginFlag = True,largeFlag = True,leftFlag = True):
    # note that tangent starts a large and finishes on sma;;
    p = svgwrite.path.Path()
    # Move Command
    if beginFlag:
        arc = 'M '+str(lines[0].__getitem__('x1'))+','+str(lines[0].__getitem__('y1'))  # start at ls[0] begin
    else:
        arc = 'M '+str(lines[0].__getitem__('x2'))+','+str(lines[0].__getitem__('y2'))  # start at ls[0] begin
    p.push(arc)
    # arc command
    radius = circle.__getitem__('r')
    arc  = ' A '+str(radius)+','+str(radius)
    arc = arc +' 0'  # flags, no rotate, small arc, to left
    if largeFlag:
        arc = arc + ' 1 '
    else:
        arc = arc + ' 0 '
    if leftFlag:
        arc = arc +' 1 '   # draw to left
    else:
        arc = arc + ' 0 '
    if beginFlag:
        arc = arc+str(lines[1].__getitem__('x1'))+','+str(lines[1].__getitem__('y1'))  # start at ls[0] begin
    else:
        arc = arc+str(lines[1].__getitem__('x2'))+','+str(lines[1].__getitem__('y2'))  # start at ls[0] begin
    p.push(arc)
    return p


