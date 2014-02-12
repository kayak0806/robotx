# Contains all classes pertaining to things on the map
import math


class Point():
    # Has an x coord (int) and a y coord (int)
    # getPos returns a tuple (x,y)
    # updatePos takes a tuple (x,y), changes x and y to match
    # distance takes a Point, returns the distance
    # inrange takes a max x and y pos, 
    #   returns trun if within a box with corners (0,0) and (x,y)
    
    def __init__(self,x,y):
      self.x = x
      self.y = y
      
    def getPos(self):
        return (self.x,self.y)
    def updatePos(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self,point):
        dx = self.x - point.x
        dy = self.y - point.y

        dist = math.sqrt(dx**2 + dy**2)
        return dist

    def inRange(self,xmax,ymax):
        if ((self.x <= xmax) and (self.y <= ymax)):
            return True
        return False
        
        
    def __str__(self):
        return "(%s,%s)"%(self.x, self.y)
        
class Item(Point):
    # Has a location (Point), a size (int)
    # getSize returns int size
    # getType retunrs string type
    # updateSize takes an int, updates the size
    # updateType takes a string, updates the type

    def __init__(self,x,y,size,type):
        Point.__init__(self,x,y)
        self.size = size
        self.type = type
        
    def getSize(self):
        return self.size
    def getType(self):
        return self.type
    def updateSize(self,size):
        self.size = size
    def updateType(self,type):
        self.type = type 

    def __str__(self):
        first = self.type+" is located at "+str(self.location)
        second =  " with radius %s"%(self.size)
        return first+second

class Obsticle(Item):
    def __init__(self,location,size):
        Item.__init__(self,location,size,"obsticle")