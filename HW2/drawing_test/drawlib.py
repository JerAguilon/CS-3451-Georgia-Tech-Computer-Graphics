# Drawing Routines, like OpenGL

from matlib import *

activeMatrix = None

def gtOrtho(left, right, bottom, top, near, far):
    print("FOOBAR")
    matrix = createIdentity()
    matrix[0][0] = 2/(right - left)
    matrix[1][1] = 2/(top - bottom)
    matrix[2][2] = -2/(far - near)
    matrix[0][3] = (right + left)/(right - left)
    matrix[1][3] = (top + bottom)/(top - bottom)
    matrix[2][3] = (far + near)/(far - near)
    activeMatrix = matrix
def gtPerspective(fov, near, far):
    matrix = createIdentity()
    
    h = n/cos(fov / 2)
    
    matrix[0][0] = 2*near/(h + h)
    matrix[1][1] = 2*near/(h + h)
    matrix[2][2] = -(far + near) / (far - near)
    matrix[3][2] = -1
    matrix[2][3] = -2 * far * near / (far - near)
    activeMatrix = matrix
    

def gtBeginShape():
    pass

def gtEndShape():
    pass

def gtVertex(x, y, z):
    topMatrix = stack.peek()
    x, y, z = multiply((x,y,z), topMatrix)
    
def multiply(vector, matrix):
    pass
