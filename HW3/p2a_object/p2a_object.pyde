 # Animation Example
from drawing_objects import Frosty, Light

time = 0   # use time to move objects from one frame to the next

    
angle = 0;

igloo = None
cam = None
frosty = None
christmasLights = [Light(i * 30, 45, -30) for i in range(5)]

class Camera(object):
    
    def __init__(self):
        self.ex = 0
        self.ey = 0
        self.ez = 0
        self.cx = 0
        self.cy = 0
        self.cz = 0
        self.ux = 0
        self.uy = 0
        self.uz = 0
    def manipulate(self, time):
        if time <= 7.28:
            cam.setEye(time * 30, 0, 150)
            cam.setCenter(time * 30, 0, 0)
    def setEye(self, x, y, z):
        self.ex = x
        self.ey = y
        self.ez = z
    def setCenter(self, x, y, z):
        self.cx = x
        self. cy = y
        self.cz = z
    def setUp(self, x, y, z):
        self.ux = x
        self.uy = y
        self.uz = z
    def disp(self):
        camera(self.ex, self.ey, self.ez, self.cx, self.cy, self.cz, self.ux, self.uy, self.uz)

class MovementGoal(object):
    def __init__(self, x, z):
        self.x = x
        self.z = z
    def hasBeenReached(self, x, z):
        return abs(self.x - x) < 1 and abs(self.z - z) < 1
    
class CascadingGoal(object):
    def __init__(self, obj, goal):
        self.goal = goal
        self.obj = obj
    def hasBeenReached(self, x, z):
        self.obj.addGoal(self.goal)
        return True

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    global igloo, cam, frosty
    igloo = loadShape("igloo2.obj")
    frosty = Frosty()
    frosty.addGoal(MovementGoal(100, 0))
    frosty.addGoal(MovementGoal(100, -30))
    cam = Camera()
    cam.setEye(0, 0, 100)
    cam.setUp(0,1,0)
def draw():
    global time, igloo, frosty
    time += 0.01
    if time >= 10000:
        time = 7.20
    walkingUp(time)
def walkingUp(time):
    global cam, frosty
        
    background (150, 150, 150)  # clear screen and set background to white
    
    # create a directional light source
    #ambientLight(50, 50, 50);
    #lightSpecular(255, 255, 255)
    ambientLight(50, 50, 50);
    for christmasLight in christmasLights:
        christmasLight.disp() 

    #ightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    noStroke()
    specular (180, 180, 180)
    #shininess (15.0)
    
    pushMatrix()
    global igloo
    translate(220,10,-300)
    scale(1, 1, 1)
    rotateY(-PI/1.5)
    rotateX(PI)
    shape(igloo) 
    popMatrix()
    
    pushMatrix()
    fill(0,0,0)
    beginShape(QUADS)
    vertex(0,60,-35)
    vertex(400,60,-35)
    vertex(400,60,-70)
    vertex(0,60,-70)
    endShape()
    popMatrix()
    
    pushMatrix()
    fill(255,255,255)
    beginShape(QUADS)
    vertex(-600,61,600)
    vertex(-600,61,-600)
    vertex(600,61,-600)
    vertex(600,61,600)
    endShape()
    popMatrix()
    
    cam.manipulate(time)
    cam.disp()
    frosty.disp(time)