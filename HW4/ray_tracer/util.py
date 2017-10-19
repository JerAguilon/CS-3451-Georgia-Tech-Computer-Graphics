class Vertex(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return "{} {} {}".format(self.x, self.y, self.z)
    def scale(self, n):
        return Vertex(self.x * n, self.y * n, self.z * n)

    def distance(self, v):
        return sqrt((v.x - self.x) ** 2 + (v.y - self.y) ** 2 + (v.z - self.z) ** 2)

    def __sub__(self, v):
        return Vertex(self.x - v.x, self.y - v.y, self.z - v.z)

    def dotProduct(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def __mul__(self, v):
        x = self.y * v.z - self.z * v.y
        y = self.z * v.x - self.x * v.z
        z = self.x * v.y - self.y * v.x
        return Vertex(x, y, z)

    def length(self):
        pre = (self.x) ** 2 + (self.y) ** 2 + (self.z) ** 2
        post = sqrt(pre)
        return post
    
    def normalize(self):
        vLength = self.length()
        return Vertex(self.x / vLength, self.y / vLength, self.z / vLength)
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
        return Vertex(x, y, z)

class Sphere(object):

    def __init__(self, r, v,red,green,blue,p):
        self.v = v
        self.r = r
        self.red = red
        self.green = green
        self.blue = blue
        self.p = p
        
    def getIntersect(self, ray):
        A = ray.slope.dotProduct(ray.slope)
        B = 2 * ( (ray.origin - self.v).dotProduct(ray.slope))
        C = (ray.origin - self.v).dotProduct(ray.origin - self.v) - self.r**2
        discriminant = B**2 - 4*A*C
        
        if discriminant < 0:
            return None
        closestSol = min(-B+sqrt(discriminant)/(2*A), -B-sqrt(discriminant)/(2*A))
        if closestSol < -.0001:
            return None
        else:
            return ray.getLocation(closestSol)
    def getNormalVector(self, v):
        return (v - self.v).normalize()
    