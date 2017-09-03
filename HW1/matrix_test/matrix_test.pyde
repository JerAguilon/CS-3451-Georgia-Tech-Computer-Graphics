# Matrix Commands

from matrix_stack import *

def setup():
    size (100, 100)
    background (255, 255, 255)
    mat_test()

# this routine tests the matrix stack command that you will implement
def mat_test():
    
    gtInitialize()
    print_ctm()
    
    gtInitialize()
    gtTranslate(3,2,1.5)
    print_ctm()

    gtInitialize()
    gtScale(2,3,4)
    print_ctm()

    gtInitialize()
    gtRotateX(90)
    print_ctm()

    gtInitialize()
    gtRotateY(-15)
    print_ctm()

    gtInitialize()
    gtPushMatrix()
    gtRotateZ(45)
    print_ctm()
    gtPopMatrix()
    print_ctm()

    gtInitialize()
    gtTranslate(1.5,2.5,3.5)
    gtScale(2,2,2)
    print_ctm()

    gtInitialize()
    gtScale(2,2,2)
    gtTranslate(1.5,2.5,3.5)
    print_ctm()

    gtInitialize()
    gtScale(2,2,2)
    gtPushMatrix()
    gtTranslate(1.5,2.5,3.5)
    print_ctm()
    gtPopMatrix()
    print_ctm()

    gtInitialize()
    gtPopMatrix()

def draw():
    pass