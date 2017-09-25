# Animation Example

time = 0   # use time to move objects from one frame to the next
pi = 3.141592653

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
angle = 0;
state = 0;

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
    pushMatrix()
    global angle, state
    if angle >= (pi * 2 - .03) and angle <= (pi * 2 + .03):
        angle = 0
        state = (state + 1) % 3
    else:
        angle = (time * 3) % (pi * 2)
    
    if state == 0:
        rotateY(angle)
    elif state == 1:
        rotateZ(angle)
    else:
        rotateX(angle)
            
    fill(139,69,19)
    pushMatrix()
    translate(8, -15, 0)
    rotateZ(-pi/20)
    hand()
    popMatrix()
    
    pushMatrix()
    translate(-8, -15, 0)
    rotateZ(pi/20)
    rotateY(pi)
    hand()
    popMatrix()

    
    # nose
    fill (255, 100, 0)
    pushMatrix()
    translate (0, -24, 0)
    scale (1, 1, 10)
    cone()
    popMatrix()
    
    # body
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
    pushMatrix()
    translate (2, -25, 6)
    cylinder()
    popMatrix()
    popMatrix()
    
    # scarf
    scarf()
    
    # hat
    pushMatrix()
    scale(5,5.8,5)
    fill (0, 0, 0)
    translate (.2, -5.5, 0)
    rotateX(pi/2)
    rotateY(pi/20)
    cylinder()
    popMatrix()
        
    pushMatrix()
    fill (0, 0, 0)
    translate (0, -28, 0)
    rotateX(pi/2)
    rotateY(pi/20)
    scale(8,8,.3)
    cylinder()
    popMatrix()
    popMatrix()

def hand():
    pushMatrix()
    scale(3,.5,1)
    rotateY(pi/2)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate(4,-1,0)
    rotateZ(-pi/5)
    scale(2,.5,1)
    rotateY(pi/2)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate(4,1,0)
    rotateZ(pi/5)
    scale(2,.5,1)
    rotateY(pi/2)
    cylinder()
    popMatrix()

def scarf(sides=64):
    # first endcap
    
    _red = (255,0,0)
    _green = (0,255,0)
    pushMatrix()
    translate (0, -20, 0)
    rotateX (pi/2)
    scale (6, 6, 1)
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
    popMatrix()
    
    fill (255, 0, 0)
    pushMatrix()
    translate(6,-17,6)
    rotateY(pi/2.5)
    rotateX(pi/4)
    rotateZ(-pi/3.9)

    box(3,3,.3)
    fill (0, 255, 0)
    translate(3,0,0)
    box(3,3,.3)

    popMatrix()

def cone(sides = 64, height = 1):
    # base circle
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 0)
    endShape(CLOSE)

    # sides
    x1 = 1
    y1 = 0
    for i in range(64):
        theta1 = i * 2 * PI / sides
        theta2 = (i + 1) * 2 * PI / sides
        x2 = cos(theta2)
        y2 = sin(theta2)
        x1 = cos(theta1)
        y1 = sin(theta1)
        beginShape(TRIANGLES)
        vertex(x1, y1, 0)
        vertex(x2, y2, 0)
        
        vertex(0,0, 1)


        endShape(CLOSE)
    
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