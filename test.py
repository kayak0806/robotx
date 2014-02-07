# For testing little things without breaking main code.
# Entire file is completly disposable

class Point:
    def __init__(self,x,y):
      self.x = x
      self.y = y
      
    def get(self):
        return (self.x,self.y)
        
    def __str__(self):
        return "(%s,%s)"%(self.x, self.y)
        
class Item:
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
  
  

def main():
    first = Point(1,2)
    print first.get()
  






if __name__ == '__main__':
    main()
