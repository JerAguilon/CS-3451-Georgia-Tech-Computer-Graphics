1# Drawing Routines, like OpenGL

from matlib import *

activeMatrix = None
vertices = []

k = -1
nearclip = -1
farclip = -1
mode = -1

def gtOrtho(left, right, bottom, top, near, far):
    global activeMatrix
    matrix_test = [[float(width)/(right - left),0,0,-left],
              [0, float(height)/(top - bottom),0,-bottom],
              [0,0,1,0],
              [0,0,0,1]]
    
    matrix1 = [[float(width)/2,0,0,float(width - 1)/2],
              [0, float(height)/2 ,0, float(height - 1) / 2],
              [0,0,1,0],
              [0,0,0,1]]
    matrix2 = [[float(2)/(right-left),0,0,-float(left+right)/2],
               [0,float(2)/(top-bottom),0,-float(bottom+top)/2],
               [0,0,1,0],
               [0,0,0,1]]
    print(matrix1)
    print(matrix2)
    finalMatrix = matrix_test#multiply(matrix1, matrix2)
    activeMatrix = finalMatrix
def gtPerspective(fov, near, far):
    global mode
    mode = 2

    k = near*tan((float(fov*pi)/180)/2)
    nearclip = near
    farclip = far
    print(k)
    print(nearclip)
    print(farclip)

def frustum(l, r, b, t, n, f):
    matrix = createIdentity()
    matrix[0][0] = 2*n/(r - l);
    matrix[1][1] = 2*n/(t - b);
    matrix[2][2] = (f + n)/(n - f);
    matrix[3][3] = 0;
    matrix[0][2] = (r + l)/(l - r);
    matrix[1][2] = (t + b)/(b - t);
    matrix[3][2] = 1;
    matrix[2][3] = 2*f*n/(f - n);
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
    
    if mode != 2:
        print("ACTIVE MATRIX: " + str(activeMatrix))
        lastVector = multiplyVector(activeMatrix, lastVector)
        currVector = multiplyVector(activeMatrix, currVector)
        
        #normalizeVector(lastVector)
        #normalizeVector(currVector)
    else:
        xstartp = nearclip*lastVector[0]/abs(lastVector[2])
        ystartp = nearclip*lastVector[1]/abs(lastVector[2])
        
        xendp = nearclip*currVector[0]/abs(lastVector[2])
        yendp = nearclip*currVector[1]/abs(lastVector[2])
        
        lastVector[0] = (xstartp+k)*width/(2*k)
        lastVector[1] = (ystartp+k)*height/(2*k)
        currVector[0] = (xendp+k)*width/(2*k)
        currVector[1] = (yendp+k)*height/(2*k)
    print("VECTORS: " + str(lastVector) + " " + str(currVector))
    line(lastVector[0], height-lastVector[1], currVector[0], height-currVector[1])
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
    