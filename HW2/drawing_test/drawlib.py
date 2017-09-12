# Drawing Routines, like OpenGL

from matlib import *

activeMatrix = None
vertices = []

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
    global vertices
    if len(vertices) == 0:
        vertices.append(multiplyVector(stack.peek(), [x,y,z,1]))
        return
    topMatrix = stack.peek()
    lastVector = multiplyVector(stack.peek(), vertices[0])
    currVector = multiplyVector(stack.peek(), [x,y,z,1])
    line(lastVector[0], currVector[0], lastVector[1], currVector[1])
    vertices = []
    
def multiplyVector(matrix, vector):
    output = []
    print(matrix)
    print(vector)
    for i in range(4):
        output.append(matrix[i][0]*vector[0] + matrix[i][1]*vector[1] + matrix[i][2]*vector[2] + matrix[i][3]*vector[3])
    return output