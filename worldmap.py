# Contains a map of the world and methods to deal with it

import items

class Map(object):
    # Takes a map size
    # Has an obsticle heat map 2d   array
    #     an object map             dictionary

    def __init__(self,sizex,sizey=None):
        if (sizey==None):
            # if no sizey, assume square
            sizey=sizex

        self.heatMap=[[0 for x in range(sizex)] for y in range(sizey)]
        self.objectMap=dict()

    # Interface
    def setHeatMap(mapIn):
        pass
    def updateObjectMap(object, location):
        pass
    

    # Utilities

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