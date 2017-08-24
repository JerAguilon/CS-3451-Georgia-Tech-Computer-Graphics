_length = 600

def setup():
    size(_length,_length)

def draw():
    background(255)
    xCoord = convertMouse(mouseX)
    yCoord = convertMouse(mouseY) # positive should be upwards
    print(str(xCoord) + "  " + str(yCoord))
    coords = powerSum(complex(xCoord, yCoord))
    
    for coord in coords:
        x = convert(coord.real)
        y = convert(-coord.imag) # positive should be upwards, but convention is flipped
        currColor = getColor(y)
        stroke(currColor[0], currColor[1], currColor[2])
        fill(currColor[0], currColor[1], currColor[2])
        ellipse(x, y, 7, 7)

# returns a rainbow given a coordinate
def getColor(coord):
    delta = _length / float(6)
    
    if coord > _length - delta:
        return (146, 0, 211)
    elif coord > _length - 2 * delta:
        return (0, 0, 255)
    elif coord > _length - 3 * delta:
        return (0, 255, 0)
    elif coord > _length - 4 * delta:
        return (255, 255, 0)
    elif coord > _length - 5 * delta:
        return (255, 127, 0)
    else:
        return (255, 0, 0)

def convert(coord):
    # from range [-3, -3]
    return (100 * coord) + _length / 2

def convertMouse(mouseCoord):
    return (mouseCoord - _length / 2)/float(150)

# returns a list of relevant points to be plotted
def powerSum(vector):
    result = []
    
    vectors = [complex(1,0)]
    
    for i in range(1, 11):
        vectors.append(vector * vectors[i - 1])
    
    powerSumRecursive(vectors, result, 0)
    return result
    
def powerSumRecursive(vectors, result, n):
    numberBranches = 2**n
    # set theory: there are 2^n elements in a power set,
    # we can allow a 0 to represent subtracting a vector and
    # 1 to represent adding a vector
    for i in range(numberBranches):
        curr = i
        counter = 0
        newVector = complex(0, 0)
        while (counter < n):
            item = curr % 2 # get the rightmost bit
            if item == 1:
                newVector += vectors[counter + 1]
            else:
                newVector -= vectors[counter + 1]
            curr = curr >> 1
            counter += 1
        result.append(newVector)
                
    if n != 10:
        powerSumRecursive(vectors, result, n + 1)
    
    
result = powerSum(complex(.664,.336))
    