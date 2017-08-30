_length = 500

# helper class for complex numbers
class Complex(object):
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __mul__(self, other):
        return Complex(
                   self.real * other.real - self.imag * other.imag,
                   self.imag * other.real + self.real * other.imag)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

def setup():
    size(_length,_length)

def draw():
    background(255)
    stroke(0)
    line(_length / 2, 0, _length / 2, _length)
    line(0, _length / 2, _length, _length / 2)
    

    stroke(153)
    # vertical markers
    line(_length / 6, 0, _length / 6, _length)
    line(2 * _length / 6, 0, 2 * _length / 6, _length)
    line(4 * _length / 6, 0, 4 * _length / 6, _length)
    line(5 * _length / 6, 0, 5 * _length / 6, _length)
    
    # horizontal markers
    line(0, _length / 6, _length, _length / 6)
    line(0, 2 * _length / 6, _length, 2 * _length / 6)
    line(0, 4 * _length / 6, _length, 4 * _length / 6)
    line(0, 5 * _length / 6, _length, 5 * _length / 6)
    
    
    xCoord = convertMouse(mouseX)
    yCoord = -convertMouse(mouseY) # positive should be upwards
    print(str(xCoord) + "  " + str(yCoord))
    coords = powerSum(Complex(xCoord, yCoord))
    print(len(coords))
    for coord in coords:
        x = convert(coord.real)
        y = convert(-coord.imag) # positive should be upwards, but convention is flipped
        currColor = getColor(y)
        stroke(currColor[0], currColor[1], currColor[2])
        fill(currColor[0], currColor[1], currColor[2])
        ellipse(x, y, 5, 5)

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
    # from  [-3, 3]
    return (_length / 6 * coord) + _length / 2

def convertMouse(mouseCoord):
    return 3 *(mouseCoord - _length / 2)/float(250)

# returns a list of relevant points to be plotted
def powerSum(vector):
    result = []
    
    vectors = [Complex(1,0)]
    
    for i in range(1, 9):
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
        newVector = Complex(0, 0)
        while (counter < n):
            item = curr % 2 # get the rightmost bit
            if item == 1:
                newVector += vectors[counter]
            else:
                newVector -= vectors[counter]
            curr = curr >> 1
            counter += 1
        result.append(newVector)
                
    if n != 9:
        powerSumRecursive(vectors, result, n + 1)    
        