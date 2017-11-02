class Vector(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return "{} {} {}".format(self.x, self.y, self.z)
    def scale(self, n):
        return Vector(self.x * n, self.y * n, self.z * n)

    def distance(self, v):
        return sqrt((v.x - self.x) ** 2 + (v.y - self.y) ** 2 + (v.z - self.z) ** 2)
    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
    def __sub__(self, v):
        return Vector(self.x - v.x, self.y - v.y, self.z - v.z)

    def dotProduct(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def __mul__(self, v):
        x = self.y * v.z - self.z * v.y
        y = self.z * v.x - self.x * v.z
        z = self.x * v.y - self.y * v.x
        return Vector(x, y, z)

    def length(self):
        pre = (self.x) ** 2 + (self.y) ** 2 + (self.z) ** 2
        post = sqrt(pre)
        return post
    
    def normalize(self):
        vLength = self.length()
        return Vector(self.x / vLength, self.y / vLength, self.z / vLength)
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

    def getLocation(self, t):
        x = self.origin.x + t * self.slope.x
        y = self.origin.y + t * self.slope.y
        z = self.origin.z + t * self.slope.z
        return Vector(x, y, z)

class Triangle(object):
    def __init__(self, vectors, dr, dg, db, ar, ag, ab, sr, sg, sb, phong, krefl):
        self.a, self.b, self.c = vectors
        
        self.dr = dr
        self. dg = dg
        self.db = db
        
        self.ar = ar
        self.ag = ag
        self.ab = ab
        
        self.sr = sr
        self.sg = sg
        self.sb = sb
        self.phong = phong
        self.krefl = krefl
        
    def getIntersect(self, ray):
        normVector = ((self.b - self.a) * (self.c - self.a)).normalize()
        dotProduct = normVector.dotProduct(ray.slope)
        if dotProduct == 0:
            # undefined
            return None
        d = normVector.dotProduct(self.a)
        t = (d - normVector.dotProduct(ray.origin)) / dotProduct
        if (t <= 0):
            return None
        
        point =  ray.getLocation(t)
        if ((self.b - self.a) * (point - self.a)).dotProduct(normVector) >= 0 \
           and ((self.c - self.b) * (point - self.b)).dotProduct(normVector) >= 0 \
           and ((self.a - self.c) * (point - self.c)).dotProduct(normVector) >= 0:
            return point
        else:
            return None
class Sphere(object):

    def __init__(self, r, v,dr, dg, db, ar, ag, ab, sr, sg, sb, phong, krefl):
        self.v = v
        self.r = r
        
        self.dr = dr
        self. dg = dg
        self.db = db
        
        self.ar = ar
        self.ag = ag
        self.ab = ab
        
        self.sr = sr
        self.sg = sg
        self.sb = sb
        
        self.phong = phong
        self.krefl = krefl
    def __repr__(self):
        return "v: {} r: {}".format(self.v, self.r)
        
    def getIntersect(self, ray):
        A = ray.slope.dotProduct(ray.slope)
        B = 2 * ( (ray.origin - self.v).dotProduct(ray.slope))
        C = (ray.origin - self.v).dotProduct(ray.origin - self.v) - self.r**2
        discriminant = B*B - 4*A*C
        #print(discriminant)
        if discriminant < 0:
            return None
        candidates = [(-B+sqrt(discriminant))/(2*A), (-B-sqrt(discriminant))/(2*A)]
        closestSol = min(candidates)
        if closestSol <= 0:#-.0001:# and self==s:
            #print(closestSol)
            return None
        
        #print("A: {} B: {} C: {} SOL: {}".format(A,B,C, closestSol))
        return ray.getLocation(closestSol)
    