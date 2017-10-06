class MovementGoal(object):
    def __init__(self, x,y, z, base=55):
        self.x = x
        self.y = y
        self.z = z
        self.base = base
    def hasBeenReached(self, x,y, z):
        return abs(self.x - x) <= 1 and abs(self.z - z) <= 1

class EquationGoal(object):
    def __init__(self, yFunc, xGoal):
        self.func = yFunc
        self.xGoal = xGoal
    def hasBeenReached(self, x):
        return x>=self.xGoal

# dummy class, doesn't need any business logic
class WiggleGoal(object):
    def __init__(self, duration):
        self.duration = duration
        self.startTime = None
        pass
    
class RotationGoal(object):
    def __init__(self, rx, ry, rz):
        self.rx = rx
        self.ry = ry
        self.rz = rz
    def hasBeenReached(self, rx, ry, rz):
        return abs(self.rx - rx) < .2 and abs(self.ry - ry) < .2 and abs(self.rz - rz) < .2