# Contains a map of the world and methods to deal with it

import items

class Map(object):
    # Has a 2d list of sizex by sizey. If no sizey specified, assume square
    #     a key dictionary maping from itemID to item type
    # self.map populated by int indicating object present at coord
    # inMap takes a point, returns true if point is in map
    # atPoint takes a point, returns the object type at that point
    # mapKey returns a dictionary of object key -> object type

    def __init__(self,sizex,sizey=None):
        if (sizey==None):
            # if no sizey, assume square
            sizey=sizex

        self.map=[[0 for x in range(sizex)] for y in range(sizey)]
        self.key={0:'water',1:'obsticle'}

    def inMap(self,point):
        xmax = len(self.map)
        ymax = len(self.map[0])

        return point.inRange(xmax,ymax)

    def atPoint(self,point):
        return self.map[point.x][point.y]

    def mapKey(self):
        return self.key

    def changeItem(self,point,item):
        itemID = self.key('')
        self.map[point.x][point.y]

    def __str__(self):
        return string2dList(self.map)


# helper functions
def string2dList(a):
    # returns a pretty formated string representing an array
    astr = ""
    if (a == []):
        # So we don't crash accessing a[0]
        return "[]"
    rows = len(a)
    cols = len(a[0])
    fieldWidth = 1
    astr+="[ "
    for row in xrange(rows):
        if (row > 0): 
            astr += "\n  "
        astr += "[ "
        for col in xrange(cols):
            if (col > 0): 
                astr+= ", "
            # The next 2 lines print a[row][col] with the given fieldWidth
            format = "%" + str(1) + "s"
            astr += format % str(a[row][col])
        astr += "]"
    astr += "]"
    return astr