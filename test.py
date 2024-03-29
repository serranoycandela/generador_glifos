import svgwrite
import math
import numpy as np

def angle2xy(centerX, centerY, radius, angleInDegrees):
  angleInRadians = (angleInDegrees-90) * math.pi / 180.0;
  x= centerX + (radius * math.cos(angleInRadians))
  y= centerY + (radius * math.sin(angleInRadians))
  return [x,y]



def addArc(dwg, current_group, p0, p1, radius):
    """ Adds an arc that cirles to the right as it moves from p0 to p1 """
    args = {'x0':p0[0],
        'y0':p0[1],
        'xradius':radius,
        'yradius':radius,
        'ellipseRotation':0, #has no effect for circles
        'x1':(p1[0]-p0[0]),
        'y1':(p1[1]-p0[1])}
    current_group.add(dwg.path(d="M %(x0)f,%(y0)f a %(xradius)f,%(yradius)f %(ellipseRotation)f 0,0 %(x1)f,%(y1)f"%args,
             fill="none",
             stroke='red', stroke_width=30
            ))


def addArcs(dwg, current_group, categories, radius, center):
    """ Adds as many as categories arcs given radius and center """

    cortesAngulares = np.linspace(0,360,categories+1)
    delta = (7/120)*cortesAngulares[1]
    for i in range(1,categories+1):
        addArc(dwg, current_group, p0=angle2xy(center[0],center[1],radius,cortesAngulares[i]-delta), p1=angle2xy(center[0],center[1],radius,cortesAngulares[i-1]+delta), radius=100)


dwg = svgwrite.Drawing(filename="test.svg", debug=True, size=(4000,1000))
current_group = dwg.add(dwg.g(id='uno', stroke='red', stroke_width=3, fill='none', fill_opacity=0 ))
centro1 = [200,200]
addArcs(dwg, current_group,3,100,centro1)
centro2 = [500,200]
addArcs(dwg, current_group,4,100,centro2)
centro3 = [800,200]
addArcs(dwg, current_group,5,100,centro3)
dwg.save()
