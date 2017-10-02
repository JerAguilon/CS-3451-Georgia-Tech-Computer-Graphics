# Animation Example

time = 0   # use time to move objects from one frame to the next

    
angle = 0;

igloo = None

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    global igloo, frosty
    igloo = loadShape("igloo2.obj")
    
def draw():
    global time, igloo, frosty
    time += 0.01
    if time >= 7.20:
        time = 7.20
    print(time)
    camera (time * 10, 0, 100 + time * 10, time * 30, 0, 0, 0,  1, 0)  # position the virtual camera

    background (220, 220, 220)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    #shininess (15.0)
    
    pushMatrix()
    global igloo
    translate(300, 0, 0)
    scale(.8, .8, .8)
    rotateY(PI)
    rotateX(PI)
    shape(igloo) 
    popMatrix()
    
    pushMatrix()
    translate(0, -abs(sin(time * 7)) * 10, 0);
    translate(-50 + time * 30, 30, 0)

    scale(.7, .7, .7)
    rotateY(PI / 2)
    rotateZ(sin(time * 7) / 5)
    frosty()
    popMatrix()

def frosty():
    pushMatrix()
    fill(139,69,19)

    translate(8, -15, 0)
    rotateZ(-PI/20)
    hand()
    popMatrix()
    
    pushMatrix()
    translate(-8, -15, 0)
    rotateZ(PI/20)
    rotateY(PI)
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
    rotateX(PI/2)
    rotateY(PI/20)
    cylinder()
    popMatrix()
        
    pushMatrix()
    fill (0, 0, 0)
    translate (0, -28, 0)
    rotateX(PI/2)
    rotateY(PI/20)
    scale(8,8,.3)
    cylinder()
    popMatrix()
def hand():
    pushMatrix()
    scale(3,.5,1)
    rotateY(PI/2)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate(4,-1,0)
    rotateZ(-PI/5)
    scale(2,.5,1)
    rotateY(PI/2)
    cylinder()
    popMatrix()
    
    pushMatrix()
    translate(4,1,0)
    rotateZ(PI/5)
    scale(2,.5,1)
    rotateY(PI/2)
    cylinder()
    popMatrix()

def scarf(sides=64):
    # first endcap
    
    _red = (255,0,0)
    _green = (0,255,0)
    pushMatrix()
    translate (0, -20, 0)
    rotateX (PI/2)
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
    rotateY(PI/2.5)
    rotateX(PI/4)
    rotateZ(-PI/3.9)

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