from goals import *

class AnimationObject(object):
    def __init__(self):
        pass
class Light(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.goals = []
        self.goalIndex = 0
    def goalsMet(self):
        return self.goalIndex == len(self.goals)    
    def addGoal(self, goal):
        self.goals.append(goal)
    def manipulate(self, time):
        print(self.goals)
        if len(self.goals) > 0 and self.goalIndex < len(self.goals):
            goal = self.goals[self.goalIndex]
            if goal.hasBeenReached(self.x, self.y, self.z):
                self.goalIndex += 1
                return
            else:
                yVector = self.y - goal.y
                dy = 0
                if yVector > .05:
                    dy = -2
                elif yVector < -.05:
                    dy = 2
                self.translate(self.x, self.y + dy, self.z)
    def translate(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def disp(self, time):
        self.manipulate(time)
        _red = (255,0,0)
        _green = (0,255,0)
        
        for i in range(10):
            fill(*(_red if i % 2 == 0 else _green))
            pushMatrix()
            translate(self.x, self.y + i * 2, self.z)
            rotateX(PI/2)
            cylinder()
            popMatrix()
        fill(255, 255, 0, 150)
        pushMatrix()
        #ambientLight(247,255,192, self.x,self.y,self.z)
        #pointLight(247,255,192, self.x, self.y, self.z)
        pointLight(247,255,192, self.x, -7, 0)

        translate(self.x, self.y - 5, self.z)
        sphere(4)
        popMatrix()

    
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
        if time <= 4:
            self.setEye(time * 30, 0, 150)
            self.setCenter(time * 30, 0, 0)
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
      
class Frosty(object):        
    def __init__(self):
        self.x = -50
        self.y = 55
        self.z = 20
        self.rx = 0
        self.ry = PI / 2
        self.rz = 0
        self.goals = []
        self.goalIndex = 0
    def goalsMet(self):
        return self.goalIndex == len(self.goals)    
    def addGoal(self, goal):
        self.goals.append(goal)
    def manipulate(self, time):
        if len(self.goals) > 0 and self.goalIndex < len(self.goals):
            goal = self.goals[self.goalIndex]
            if type(goal) is MovementGoal:
                if goal.hasBeenReached(self.x,self.y, self.z):
                    self.goalIndex += 1
                    self.rotate(0, self.ry, 0)
                    self.translate(self.x, 55, self.z)
                    return
                else:
                    xVector = goal.x - self.x
                    zVector = goal.z - self.z
                    baseVector = [0, 1]
                    if xVector == 0 and zVector == 0:
                        angle = self.ry
                    else:
                        angle = acos(baseVector[0] * xVector + baseVector[1] * zVector / (xVector**2 + zVector**2)**.5) % (2*PI)
                    diff = self.ry - angle
                    if diff > .2 or diff < -.2:
                        if diff < 0:
                            self.rotate(0, self.ry + .05, 0)
                        else:
                            self.rotate(0, self.ry - .05, 0)
                    else:
                        dx = 0
                        dz = 0
                        if xVector < 0:
                            dx = -.5
                        elif xVector > 0:
                            dx = .5
                        if zVector < 0:
                            dz = -.5
                        elif zVector > 0:
                            dz = .5
                        self.translate(self.x + dx, 55 - abs(sin(time * 7) * 8), self.z + dz)
                        self.rotate(0, angle, sin(time * 7) / 5)
            elif type(goal) is RotationGoal:
                import random
                print(random.randint(1,20))
                if goal.hasBeenReached(self.rx, self.ry, self.rz):
                    self.goalIndex += 1
                    return
                else:
                    rotation = self.ry
                    diff = rotation - goal.ry
                    print("{} {} --> {}".format(rotation, self.ry, diff))
                    if diff < 0:
                        self.rotate(0, self.ry + .2, 0)
                    else:
                        self.rotate(0, self.ry - .2, 0)
            else:
                if goal.hasBeenReached():
                    self.goalIndex += 1
                    return

    def translate(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def rotate(self, x, y, z):
        # order of rotation: z y x
        self.rz = z
        self.ry = y
        self.rx = x
    def disp(self, time):
        self.manipulate(time)
        pushMatrix()
        translate(self.x, self.y, self.z);
        scale(.7, .7, .7)
        rotateX(self.rx)
        rotateY(self.ry)
        rotateZ(self.rz)
        self.makeSnowman()
        popMatrix()
    def makeSnowman(self):
        pushMatrix()
        fill(139,69,19)
        translate(8, -15, 0)
        rotateZ(-PI/20)
        self.hand()
        popMatrix()
        
        pushMatrix()
        translate(-8, -15, 0)
        rotateZ(PI/20)
        rotateY(PI)
        self.hand()
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
        self.scarf()
        
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
    def hand(self):
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

    def scarf(self, sides=64):
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