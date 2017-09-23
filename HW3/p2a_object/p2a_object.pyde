# Animation Example

time = 0   # use time to move objects from one frame to the next
pi = 3.141592653

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01

    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (220, 220, 220)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    #shininess (15.0)
    
    # # red box
    # fill (255, 0, 0)
    # pushMatrix()
    # translate (-30, 0, 0)
    # rotateX (time)
    # box(20)
    # popMatrix()

    # # green sphere
    # fill (0, 250, 0)
    # pushMatrix()
    # translate (0, 8 * sin(4 * time), 0)  # move up and down
    # sphereDetail(60)  # this controls how many polygons are used to make a sphere
    # sphere(10)
    # popMatrix()

    # # blue cylinder
    # fill (0, 0, 255)
    # pushMatrix()
    # translate (30, 0, 0)
    # rotateX (-time)
    # scale (10, 10, 10)
    # cylinder()
    # popMatrix()
    
    pushMatrix()
    rotateY(1)
    
    fill (255, 255, 255)
    pushMatrix()
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(10)
    popMatrix()
    
    pushMatrix()
    translate (0, -13, 0)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(8)
    popMatrix()
    
    pushMatrix()
    translate (0, -25, 0)
    sphereDetail(60)  # this controls how many polygons are used to make a sphere
    sphere(6)
    popMatrix()

    # eyes
    pushMatrix()
    scale(1,1,.9)
    fill (0, 0, 0)
    pushMatrix()
    translate (-2, -25, 6)
    cylinder()
    popMatrix()
    fill (0, 0, 0)
    pushMatrix()
    translate (2, -25, 6)
    cylinder()
    popMatrix()
    popMatrix()
    
    # scarf
    fill (0, 0, 0)
    pushMatrix()
    translate (0, -20, 0)
    rotateX (pi/2)
    scale (6, 6, 1)
    scarf()
    popMatrix()
        
    popMatrix()

def scarf(sides=64):
    # first endcap
    
    _red = (255,0,0)
    _green = (0,255,0)
    beginShape()
    for i in range(sides):
        if int(i/4) % 2 == 0:
            fill(*_red)
        else:
            fill(*_green)
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        if int(i/4) % 2 == 0:
            fill(*_red)
        else:
            fill(*_green)
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        if int(i/4) % 2 == 0:
            fill(*_red)
        else:
            fill(*_green)
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2