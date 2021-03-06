# TangentUtilities
## History
When learning the Python package **svgwrite** I soon discovered that I needed the ability to draw tangents between circles.
There is no such functionality built into svgwrite and I could not find anything useful out there.
**Inkscape** has plugins for tangents but they are not relevant to the person using svgwrite
## My Solution
The need to draw tangents is not just applicable to svgwrite so I created a general purpose module called **TangentUtilities**.
Then I created an interface from svgutils to TangentUtilities
## Details
**TangentUtilities** defines basic classes, **Point, Line, Rectangle, rectTriangle and Circle**. I trust their names and meanings are self explanatory.
A Circle can easily be contructed from an svgwrite Circle shape from its center and radius attributes.  
The Tangent function accepts 2 Circles as parameters and returns a pair of Lines. An svgwrite Line shape can easily be constructed from these Lines.
### Point
A single point in the xy 2 dimensional plane with the properties x and y (float)
### Line
Has 2 explicit properties **begin** and **end**. They are both **Points**. From these we derive the implicit property **slope**. Angles in the xy
plane increase in an anticlockwise diretion.
### Circle
Has 2 explicit properties, **center** which is a **Point** and **radius** (float)
### Rectangle
A rectangle is constructed from an initial **Line** and the length of the next line perpendicular to the first line. The **buildOrder** of clockwise or anticlockwise defines whether the slope of one line is +90 degrees or -90 degrees to its predecessor.  
After construction there is the property **sides** which is an array of 4 **Lines**. The 1st side (side[0]) is the original Line used in construction.
### The Maths
Nothing complicated, just basic high school geometry. The trick is to make it work in all cases of the relative positions between the circles e.g. is the smaller circle to the left or to the right of the larger? Directly above or directly below?  
We start by defining a quadrangle outlined by:  
1. The tangent
1. The line joining the 2 circles centers (called H1 in my code). 
1. The radii joining the circle centers and the contact points of the tangent

In the case of the 2 radii being the same the tangent is parallel to H1 and the quadrangle is in fact a rectangle.  
In the case of the 2 radii being different the tangent diverges from H1. My method divides the quadrangle into a rectangle and a right angled triangle.
Knowing the the basic properties of the rectangle, its first line begin and end points and the length of the second line, it is simple to calculate the properties of all the lines of the rectangle.
The tanget is the 3rd line in the array of 4 lines.
The solution must be applied twice for the 2 tangents, once by calculating the rectangle in a clockwise direction and then in an antoclockwise direction
## Future
This is a work in progress. Superfluous code will be eliminated and the test scripts cleaned up. I welcome feedback, especially bugs.  
At the time of writing, only external tangents are calculated, Internal tangents are TBD.
