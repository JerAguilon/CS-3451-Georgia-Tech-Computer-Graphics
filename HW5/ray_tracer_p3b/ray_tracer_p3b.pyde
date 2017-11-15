# This is the starter code for the CS 3451 Ray Tracing project.
#
# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.
from util import *


shapes = []
vertices = []
lightSources = []
backgroundColor = (0,0,0)
diffuseColor = (0,0,0)
ambientColor = (0,0,0)
specularColor = (0,0,0)
phong = 0
krefl = 0
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
    elif key == '0':
        interpreter("i10.cli")

def interpreter(fname):
    global shapes, lightSources, backgroundColor, diffuseColor, fov, \
           ambientColor, specularColor, phong, krefl, vertices
    
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
            print("ADDING SPHERE")
            radius = float(words[1])
            x = float(words[2])
            y = float(words[3])
            z = float(words[4])
            v = Vector(x,y,z)
            shapes.append(Sphere(radius, v, 
                                 diffuseColor[0], diffuseColor[1], diffuseColor[2],
                                 ambientColor[0], ambientColor[1], ambientColor[2],
                                 specularColor[0], specularColor[1], specularColor[2],
                                 phong, krefl))
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
            
            ar = float(words[4])
            ag = float(words[5])
            ab = float(words[6])
            ambientColor = (ar, ag, ab)
            
            sr = float(words[7])
            sg = float(words[8])
            sb = float(words[9])
            specularColor = (sr, sg, sb)
            
            phong = float(words[10])
            krefl = float(words[11])
        elif words[0] == 'begin':
            vertices = []
        elif words[0] == 'vertex':
            vertices.append(Vector(float(words[1]), float(words[2]), float(words[3])))
        elif words[0] == 'end':
            shapes.append(Triangle(vertices,
                                 diffuseColor[0], diffuseColor[1], diffuseColor[2],
                                 ambientColor[0], ambientColor[1], ambientColor[2],
                                 specularColor[0], specularColor[1], specularColor[2],
                                 phong, krefl))
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])  # write the image to a file
            shapes = []
            lightSources = []
            backgroundColor = (0,0,0)
            diffuseColor = (0,0,0)
            specularColor = (0,0,0)
            phong = 0
            krefl = 0
            fov = 0
            pass

# render the ray tracing scene
def render_scene():
    debugX = 128
    debugY = 132
    
    print(fov)
    k = tan(radians(fov/2))
    for j in range(height):
        print(j)
        for i in range(width):
            if height - j == debugY and i == debugX:
                debug = True
            else:
                debug = False
            
            transY = (j - height / 2) * 2*k / (height)
            transX = (i - width / 2) * 2*k / (width)
            v1 = Vector(0,0,0)
            v2 = Vector(transX, transY, -1)
            
            ray = Ray(v1, v2)
            candidates = []
            for s in shapes:
                curr = s.getIntersect(ray)
                if curr != None:
                    distance = curr.distance(ray.origin)
                    candidates.append((distance, curr, s))
            if len(candidates) == 0:
                pix_color = color(*backgroundColor)
                set(i,height-j, pix_color)
            else:
                #print(candidates)
                bestPoint, s = min(candidates)[1:3]
                pixColor = getColor(ray, s, bestPoint, debug)
                pix_color = color(*pixColor)
                set(i,height-j,pix_color)
            continue

def getColor(ray, s, bestPoint, debug):
    if debug:
        print("DEBUGGING")
        print(s)
    
    output = [0,0,0]
    
    if type(s) is Sphere:
        normVector = (bestPoint - s.v).normalize()
    else:
        # gotta be a triangle
        normVector = ((s.b - s.a) * (s.c - s.a)).normalize().scale(-1)
    if s.krefl > 0:
        if debug:
            print("REFLECTING")
        normRay = ray.slope.normalize()
        reflectedVector = (normVector.scale(2 * normVector.dotProduct(normRay)) - normRay).scale(-1)
        reflection = Ray(bestPoint, reflectedVector)
        
        if debug:
            print("~~~~~~~~~~~~~~~~~~~~~~");
            print(reflection.origin)
            print(reflection.slope)
            print("~~~~~~~~~~~~~~~~~~~~~~")
        
        candidates = []
        for currShape in shapes:
            if currShape == s:
                continue
            curr = currShape.getIntersect(reflection)
            if curr != None:
                distance = curr.distance(bestPoint)
                candidates.append((distance, curr, currShape))
        if len(candidates) == 0:
            output[0] += s.krefl * backgroundColor[0]
            output[1] += s.krefl * backgroundColor[1]
            output[2] += s.krefl * backgroundColor[2]
        else:
            if debug:
                print("CANDIDATES")
                print(candidates)
            nextObj = min(candidates)
            recursiveColor = getColor(reflection, nextObj[2], nextObj[1], debug)
            output[0] += s.krefl * recursiveColor[0]
            output[1] += s.krefl * recursiveColor[1]
            output[2] += s.krefl * recursiveColor[2]    
    # output[i] = ambient[i] + cosineAngle * diffuse[i] * light[i] + [TODO Phong] + krefl[i] * outputNext[i]
    output[0] += s.ar    
    output[1] += s.ag
    output[2] += s.ab
    
    for light in lightSources:
        lightVector = (light.v - bestPoint).normalize()
        
        isCovered = False
        # find overshadowing objects
        if type(s) in [Sphere, Triangle]:
            for currShape in shapes:
                
                offset = lightVector.scale(-.00001)
                choice1 = bestPoint + offset
                choice2 = bestPoint - offset
                
                # maximize the dist.from the object
                if type(s) is Sphere:
                    if s.v.distance(choice1) > s.v.distance(choice2):
                        choice = choice1
                    else:
                        choice = choice2
                else:
                    if light.v.distance(choice1) < light.v.distance(choice2):
                        choice = choice1
                    else:
                        choice = choice2                 
                currPoint = currShape.getIntersect(Ray(choice, lightVector))
                # currPoint can't be behind light
                if currPoint != None \
                   and (bestPoint.distance(currPoint) < bestPoint.distance(light.v)):
                    isCovered = True
        if not isCovered:                      
            proportion = max(normVector.dotProduct(lightVector), 0)
            output[0] += s.dr * light.r * proportion
            output[1] += s.dg * light.g * proportion
            output[2] += s.db * light.b * proportion
            
            e = (ray.origin - bestPoint).normalize() # surface to eye
            l = (light.v - bestPoint).normalize() # light to surface
            # r = normVector.scale(2 * (l.dotProduct(normVector))) - l
            
            h = (e + l).normalize()
            factor = h.dotProduct(normVector)**s.phong
            # factor = max(0, e.dotProduct(r))**s.phong
            output[0] += s.sr * light.r * factor
            output[1] += s.sg * light.g * factor
            output[2] += s.sb * light.b * factor    
    return output

# should remain empty for this assignment
def draw():
    pass