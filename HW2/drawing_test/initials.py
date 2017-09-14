# In the routine below, you should draw your initials in perspective

from matlib import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective(60,-100,100)
    gtPushMatrix()
    gtTranslate(0, .8, -4)

    gtRotateX(50)
    gtRotateY(10)
    #J
    
    gtBeginShape()
    # Front J
    gtVertex(-.5,  1.0,  1.0)
    gtVertex( .5,  1.0,  1.0)

    gtVertex(0, 1.0, 1.0)
    gtVertex(0, 0, 1)
    
    gtVertex(0, 0, 1)
    gtVertex(-.9,0, 1)
    
    gtVertex(-.9,0, 1)
    gtVertex(-.9,.25,1)
    # Back J
    gtVertex(-.5,  1.0,  .7)
    gtVertex( .5,  1.0,  .7)

    gtVertex(0, 1.0, .7)
    gtVertex(0, 0, .7)
    
    gtVertex(0, 0, .7)
    gtVertex(-.9,0, .7)
    
    gtVertex(-.9,0, .7)
    gtVertex(-.9,.25,.7)

    gtEndShape()
    
    #A
    gtBeginShape()
    #frontA
    gtVertex( .5,  1.0,  1.0)
    gtVertex( .4,  0,  1.0)

    gtVertex( .5,  1.0,  1.0)
    gtVertex( .8,  0,  1.0)
    
    gtVertex(.47,  .7,  1.0)
    gtVertex(.59,  .7,  1.0)

    #back A
    gtVertex( .5,  1.0,  .7)
    gtVertex( .4,  0,  .7)

    gtVertex( .5,  1.0,  .7)
    gtVertex( .8,  0,  .7)
    
    gtVertex(.47,  .7,  .7)
    gtVertex(.59,  .7,  .7)

    gtEndShape()
    gtPopMatrix()