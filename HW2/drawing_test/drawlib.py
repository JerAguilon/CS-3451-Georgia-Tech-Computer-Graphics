1# Drawing Routines, like OpenGL

from matlib import *

vertices = []

k = -1
nearclip = -1
farclip = -1
mode = -1

lleft = -1
rright = -1
ttop = -1
bbottom = -1

ffov = -1
nnear = -1
ffar = -1

def gtOrtho(left, right, bottom, top, near, far):
    global lleft
    global rright
    global ttop
    global bbottom
    global mode
    
    lleft = left
    rright = right
    bbottom = bottom
    ttop = top
    
    mode = 1
def gtPerspective(fov, near, far):
    global mode, ffov, nnear, ffar
    mode = 2
    ffov = fov
    nnear = near
    ffar = ffar

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
    pass

def gtEndShape():
    pass

def gtVertex(x, y, z):
    global mode
    global vertices
    if len(vertices) == 0:
        vertices.append([x,y,z,1])
        return
    topMatrix = stack.peek()
    lastVector = multiplyVector(stack.peek(), vertices[0])
    currVector = multiplyVector(stack.peek(), [x,y,z,1])
    
    
    if mode == 1:
        global ttop, bbottom, lleft, rright
        lastVector[0] = float(lastVector[0] - lleft) / (rright - lleft) * width
        lastVector[1] = float(lastVector[1] - bbottom) / (ttop - bbottom) * height
        
        currVector[0] = float(currVector[0] - lleft) / (rright - lleft) * width
        currVector[1] = float(currVector[1] - bbottom) / (ttop - bbottom) * height
    else:
        global ffov
        print(" PREVVECTORS {} {}".format(lastVector, currVector))

        lastVectorPerspX = float(lastVector[0]) / abs(lastVector[2])
        lastVectorPerspY = float(lastVector[1]) / abs(lastVector[2])
        
        currVectorPerspX = float(currVector[0]) / abs(currVector[2])
        currVectorPerspY = float(currVector[1]) / abs(currVector[2])
        
        radFov = ffov * pi / 180
        k = tan(radFov/2)
        print("K: " + str(k))
        lastVector[0] = (float(lastVectorPerspX + k)) * (width / float(2*k))
        lastVector[1] = (float(lastVectorPerspY + k)) * (height / float(2*k))
        currVector[0] = (float(currVectorPerspX + k)) * (width / float(2*k))
        currVector[1] = (float(currVectorPerspY + k)) * (height / float(2*k))
        print(" VECTORS {} {}".format(lastVector, currVector))
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
    