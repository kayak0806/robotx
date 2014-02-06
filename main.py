# Main run file


class Point:
    # Has an x coord (int) and a y coord (int)
    # Get returns a tuple (x,y)
    #!! distance takes a Point, returns the distance
    
    def __init__(self,x,y):
      self.x = x
      self.y = y
      
    def get(self):
        return (self.x,self.y)
    
    def distance(self,point):
    #!!
        return 0 
        
        
    def __str__(self):
        return "(%s,%s)"%(self.x, self.y)
        
class Item:
    # Has a location (Point), a size (int), and a title (str)
    # Get[x] returns x
    
    def __init__(self,location,size,title):
        self.location = location
        self.size = size
        self.title = title
        
    def getLocation(self):
        return self.location
    def getSize(self):
        return self.size
    def getTitle(self):
        return self.title

    def __str__(self):
        first = self.title+" is located at "+str(self.location)
        second =  " with radius %s"%(self.size)
        return first+second

class Obsticle(Item):
    def __init__(self,location,size):
        Item.init(location,size,"obsticle")
    
    def distance
  
  

def main():
    
    myItem = Item(Point(1,1),2,"obsticle")
    print myItem
    
    # Planned order of operations:
    #   recive info
    #   plan out path
    #   send path back
  






if __name__ == '__main__':
  main()
