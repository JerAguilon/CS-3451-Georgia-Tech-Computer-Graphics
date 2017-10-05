 # Jeremy Aguilon
from drawing_objects import Frosty, Light, Camera
from goals import *

time = 0   # use time to move objects from one frame to the next

    
angle = 0;

snow = None
igloo = None
sleigh = loadImage("SantasSleigh.obj")
cam = Camera()
frosty = Frosty()
christmasLights = [Light(i * 30, 45, -30) for i in range(5)]

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    global igloo, cam, frosty, snow, sleigh
    igloo = loadShape("igloo2.obj")
    snow = loadImage("snow.jpg")
    #sleigh = loadImage("SantasSleigh.obj")
    frosty.addGoal(MovementGoal(85, 55, 20))
    frosty.addGoal(MovementGoal(100, 55, -30))
    frosty.addGoal(RotationGoal(0, 0, 0))
    frosty.addGoal(CascadingGoal(christmasLights[4], MovementGoal(90, 20, -30)))
    print("FROSTY {}".format(frosty))
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
    global cam, frosty, igloo, sleigh
        
    background (150, 150, 150)  # clear screen and set background to white
    
    ambientLight(50, 50, 50);
   # lightSpecular(255, 255, 255)
    #pointLight(255, 255, 255, 0, 40, 36);
    pointLight(255, 255, 255, 20, -40, 40);
    #pointLight(255, 255, 255, -10, -10, 10);
    #pointLight(255, 255, 255, -20, 40, 30);
    directionalLight (255, 255, 255, 0, 10, 35)
    #directionalLight (255, 255, 255, 40 - 25 * time, -5, 10)
    #lightSpecular(255, 255, 255)   
    for christmasLight in christmasLights:
        christmasLight.disp(time) 

    #ightSpecular(255, 255, 255)
    #directionalLight (100, 100, 100, -0.3, 0.5, -1)
    # noStroke()
    # specular (180, 180, 180)
    # pushMatrix()
    # translate(100,10,-300)
    # scale(1, 1, 1)
    # rotateY(-PI/1.5)
    # rotateX(PI)
    # shape(igloo) 
    # popMatrix()
    
    noStroke()
    specular (180, 180, 180)
    shininess(15.0)
    pushMatrix()
    scale(100, 100, 100)
    rotateY(-PI/1.5)
    rotateX(PI)
    shape(sleigh) 
    popMatrix()
    
    
    global img
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
    translate(-100,61,-100)
    rotateX(PI/2)
    beginShape(QUADS)
    texture(snow)
    vertex(0,0,0,0)
    vertex(300,0,0,401)
    vertex(300,100,620,401)
    vertex(0,100,620,0)
    endShape()
    popMatrix()
    
    pushMatrix()
    translate(200,61,-100)
    rotateZ(PI/10)
    rotateX(PI/2)
    beginShape(QUADS)
    texture(snow)
    vertex(0,0,0,0)
    vertex(100,0,0,401)
    vertex(100,100,620,401)
    vertex(0,100,620,0)
    endShape()
    popMatrix()
    
    pushMatrix()
    translate(200,61,-100)
    rotateZ(PI/10)
    rotateX(PI/2)
    beginShape(QUADS)
    texture(snow)
    vertex(0,0,0,0)
    vertex(100,0,0,401)
    vertex(100,100,620,401)
    vertex(0,100,620,0)
    endShape()
    popMatrix()
    
    
    cam.manipulate(time)
    cam.disp()
    frosty.disp(time)