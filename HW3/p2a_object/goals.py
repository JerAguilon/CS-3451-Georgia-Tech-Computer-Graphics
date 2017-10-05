class MovementGoal(object):
    def __init__(self, x,y, z):
        self.x = x
        self.y = y
        self.z = z
    def hasBeenReached(self, x,y, z):
        return abs(self.x - x) <= 1 and abs(self.z - z) <= 1
    
class CascadingGoal(object):
    def __init__(self, obj, goal):
        self.goal = goal
        self.obj = obj
    def hasBeenReached(self):
        self.obj.addGoal(self.goal)
        print("ADDED GOAL: {}".format(self.obj))
        return True
    
class RotationGoal(object):
    def __init__(self, rx, ry, rz):
        self.rx = rx
        self.ry = ry
        self.rz = rz
    def hasBeenReached(self, rx, ry, rz):
        return abs(self.rx - rx) < .2 and abs(self.ry - ry) < .2 and abs(self.rz - rz) < .2