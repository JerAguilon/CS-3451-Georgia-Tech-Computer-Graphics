# This is the starter code for the CS 3451 Ray Tracing project.
#
# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.

shapes = []
lightSources = []
backgroundColor = (0,0,0)
diffuseColor = (0,0,0)
fov = 0

def setup():
    size(500, 500) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

# read and interpret the appropriate scene description .cli file based on key press
def keyPressed():
    if key == '1':
        interpreter("i1.cli")
    elif key == '2':
        interpreter("i2.cli")
    elif key == '3':
        interpreter("i3.cli")
    elif key == '4':
        interpreter("i4.cli")
    elif key == '5':
        interpreter("i5.cli")
    elif key == '6':
        interpreter("i6.cli")
    elif key == '7':
        interpreter("i7.cli")
    elif key == '8':
        interpreter("i8.cli")
    elif key == '9':
        interpreter("i9.cli")

def interpreter(fname):
    global shapes, lightSources, backgroundColor, diffuseColor, fov
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            Vector v = Vector(x,y,z)
            shapes.append(Sphere(radius, v))
            # call your sphere creation routine here
            # for example: create_sphere(radius,x,y,z)
        elif words[0] == 'fov':
            fov = float(words[1])
            pass
        elif words[0] == 'background':
            r = float(words[1])
            g = float(words[2])
            b = float(words[3])
            backgroundColor = (r,g,b)
            pass
        elif words[0] == 'light':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            r = float(words[4])
            g = float(words[5])
            b = float(words[6])
            v = Vector(x,y,z)
            
            light = LightSource(v,r,g,b)
            lightSources.append(light)
            pass
        elif words[0] == 'surface':
            dr = float(words[1])
            dg = float(words[2])
            db = float(words[3])
            diffuseColor = (dr,dg,db)
            pass
        elif words[0] == 'begin':
            pass
        elif words[0] == 'vertex':
            pass
        elif words[0] == 'end':
            pass
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    for j in range(height):
        for i in range(width):
            # create an eye ray for pixel (i,j) and cast it into the scene
            pix_color = color(0.8, 0.2, 0.4)  # you should calculate the correct pixel color here
            set (i, j, pix_color)         # fill the pixel with the calculated color
    pass

# should remain empty for this assignment
def draw():
    pass