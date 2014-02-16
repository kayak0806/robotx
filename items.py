# Contains all classes pertaining to things on the map
import math
import datetime


class Point(object):
    # Has an x coord (int) and a y coord (int)
    # getPos returns a tuple (x,y)
    # updatePos takes a tuple (x,y), changes x and y to match
    # getChange takes a Point, 
    #   returns (distance between points, direction of the second point)
    # inrange takes a max x and y pos, 
    #   returns true if within a box with corners (0,0) and (x,y)
    
    def __init__(self,x,y):
      self.x = x
      self.y = y
      
    def getPos(self):
        return (self.x,self.y)
    def updatePos(self,x,y):
        self.x = x
        self.y = y

    def getChange(self,point):
        dx = self.x - point.x
        dy = self.y - point.y
        dist = math.sqrt(dx**2 + dy**2)

        direction = 0
        return (dist,direction)    

    def inRange(self,xmax,ymax):
        if ((self.x <= xmax) and (self.y <= ymax)):
            return True
        return False        
        
    def __str__(self):
        return "(%s,%s)"%(self.x, self.y)
 
class Body(object):
    # pos: Point
    def __init__(self,pos,id=1):
        self.pos = pos
        self.id = 1             #TODO Get ID

    def getPos(self):
        return self.pos
    def getID(self):
        return self.id


class Boat(Body):
    # Has a location (Point), a direction (float)
    # getDir, getPos

    def __init__(self,pos,directionFacing):
        Body.__init__(self,pos,1)
        self.direction = directionFacing
        
    def getDir(self):
        return self.direction
    def updateDir(self,newDir):
        self.direction = newDir

    def __str__(self):
        return "boat is located at "+self.pos.__str__()

class Gate(Body):
    def __init__(self, portPoint, starboardPoint):
        Body.__init__(self,portPoint)
        self.starboardPos = starboardPoint
        self.len,self.direction = self.pos.getChange(self.starboardPos)
        self.done = False

    def updatePoint(side, newPoint):
        if side == 'port':
            self.portPoint.updatePos(newPoint)
        if side == 'starboard':
            self.starboardPoint.updatePos(newPoint)

    def crossed(self):
        # TODO
        return False

    def __str__(self):
        portStr = self.pos.__str__()
        starStr = self.starboardPos.__str__()
        return "gate is located between "+portStr+" and "+starStr

class WaitPoint(Body):
    def __init__(self,pos,tolerance):
        Body.__init__(self,pos)
        self.tolerance = tolerance
        self.done = False

    def done(self):
        # TODO
        return False

    def __str__(self):
        return "Wait at "+self.pos.__str__()

def main():
    # For testing things
    myBoat = Boat(Point(2,3),0)
    print myBoat
    myGate = Gate(Point(0,0),Point(0,3))
    print myGate
    myWait = WaitPoint(Point(5,6),3)
    print myWait

if __name__ == '__main__':
    main()
