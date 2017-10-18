class Vertex(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def distance(self, v):
        return sqrt( (v.x - self.x)**2 + (v.y - self.y)**2 + (v.z - self.z)**2)    
    
    def subtract(self, v):
        return Vertex(self.x - v.x, self.y - v.y, self.z - v.z)

    def dotProduct(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z
    
    def crossProduct(self, v):
        x = self.y * v.z - self.z * v.y
        y = self.z * v.x - self.x*v.z
        z = self.x*v.y - self.y*v.x
        return Vertex(x,y,z)
    
    def __len__(self):
        return sqrt( (self.x)**2 + (self.y)**2 + (self.z)**2) 

class LightSource(object):
    def __init__(self, v, r, g, b):
        self.v = v
        self.r = r
        self.g = g
        self.b = b

class Ray(object):
    def __init__(self, origin, slope):
        self.origin = origin
        self.slope = slope
    def getLocation(self, time):
        x = self.origin.x + t*self.slope.x
        y = self.origin.y + t*self.slope.y
        z = self.origin.z + t*self.slope.z
        return Vertex(x,y,z)
    
class Sphere(object):
    def __init__(self, r, v, cdr, cdg, cdb):
        self.v = v
        self.r = r
        self.cdr = cdr
        self.cdg = cdg
        self.cdb = cdb