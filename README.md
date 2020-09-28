# TangentUtilities
## History
When learning the Python package **svgwrite** I soon discovered that I needed the ability to draw tangents between circles.
There is no such functionality built into svgwrite and I could not find anything useful out there.
**Inkscape** has plugins for tangents but they are not relevant to the person using svgwrite
## My Solution
The need to draw tangents is not just applicable to svgwrite so I created a general purpose package called **TangentUtilities**.
Then I created and interface from svgutils to TangentUtils
## Details
**TangentUtilities** defines its basic classes, **Point, Line, Rectangle, rectTriangle and Circle**. I trust their names and meanings are self explanatory.
A Circle can easily be contructed from an svgwrite Circle shape from its center and radius attributes.
The Tangent function accepts 2 Circles as parameters and returns a pair of Lines. An svgwrite Line shape can easily be constructed from these Lines.
