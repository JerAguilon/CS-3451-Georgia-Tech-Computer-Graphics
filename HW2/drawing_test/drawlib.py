1# Drawing Routines, like OpenGL

from matlib import *

activeMatrix = None
vertices = []
mode = -1

minX = -1
maxX = -1
minY = -1
maxY = -1

def gtOrtho(left, right, bottom, top, near, far):
    global mode
    global activeMatrix
    global minX
    global maxX
    global minY
    global maxY
    
    minX = left
    maxX = right
    minY = bottom
    maxY = top
    mode = 1
    # matrix1 = [[float(width)/2,0,0,float(width - 1) / 2],
    #           [0, float(height)/2,0, float(height - 1) / 2],
    #           [0,0,1,0],
    #           [0,0,0,1]]
    # matrix2 = [[2/float(right - left),0,0,0],
    #            [0,2/float(top - bottom),0,0],
    #            [0,0,2/float(near - far),0],
    #            [0,0,0,1]]
    # matrix3 = [[1,0,0,float(left + right) / -2],
    #            [0,1,0, float(bottom + top) / -2],
    #            [0,0,1, float(near + far) / -2],
    #            [0,0,0,1]]
    # finalMatrix = multiply(matrix1, multiply(matrix2, matrix3))
    finalMatrix = createIdentity()
    finalMatrix[0][0] = 2/float(right - left);
    finalMatrix[1][1] = 2/float(top - bottom);
    finalMatrix[2][2] = -2/float(far - near);
    finalMatrix[0][3] = float(right + left)/(right - left);
    finalMatrix[1][3] = float(top + bottom)/(top - bottom);
    finalMatrix[2][3] = float(far + near)/(far - near);
    print("FINAL MATRIX: " + str(finalMatrix))
    activeMatrix = finalMatrix
def gtPerspective(fov, near, far):
    global mode
    global activeMatrix
    mode = 2
    h = float(near)/cos(fov / 2)
    activeMatrix = frustum(-h, h, -h, h , near,far)

def frustum(l, r, b, t, n, f):
    matrix = createIdentity()
    matrix[0][0] = 2*n/(r - l);
    matrix[1][1] = 2*n/(t - b);
    matrix[2][2] = -(f + n)/(f - n);
    matrix[3][3] = 0;
    matrix[0][2] = (r + l)/(r - l);
    matrix[1][2] = (t + b)/(t - b);
    matrix[3][2] = -1;
    matrix[2][3] = -2*f*n/(f - n);
    return matrix

def gtBeginShape():
    global vertices
    vertices = []


def gtEndShape():
    global vertices
    vertices = []

def gtVertex(x, y, z):
    global mode
    global vertices
    if len(vertices) == 0:
        vertices.append([x,y,z,1])
        return
    topMatrix = stack.peek()
    lastVector = multiplyVector(stack.peek(), vertices[0])
    currVector = multiplyVector(stack.peek(), [x,y,z,1])
    print("ACTIVE MATRIX: " + str(activeMatrix))
    lastVector = multiplyVector(activeMatrix, lastVector)
    currVector = multiplyVector(activeMatrix, currVector)
    normalizeVector(lastVector)
    normalizeVector(currVector)
    print("VECTORS: " + str(lastVector) + " " + str(currVector))
    line(lastVector[0] * width / 2, lastVector[1] * height / 2, currVector[0] * width / 2, currVector[1] * height / 2)
    vertices = []
    
def multiplyVector(matrix, vector):
    output = []
    for i in range(4):
        output.append(matrix[i][0]*vector[0] + matrix[i][1]*vector[1] + matrix[i][2]*vector[2] + matrix[i][3]*vector[3])
    return output

def normalizeVector(vector):
    scaler = vector[3]
    
    for i in range(4):
        vector[i] /= scaler
    