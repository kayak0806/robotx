'''
	Importaint:
	Main must take a stdin input
	In terminal:
	echo <input> | pyhton main.py
	OR
	cat <filename>.txt | python main.py
'''

# Main run file
import math
import fileinput
import sys
import items
import worldmap

def parseStr(arrayStr):
	# Take a string containing an array
	# Return the array
	return eval(arrayStr)

def getInput():
	# Read from stdin
	# Return a tuple of the given inputs

	# World is a list of lists representing the world
	arrayStr = ""
	for line in fileinput.input():
		line=line.rstrip()
		arrayStr += line
	world = parseStr(arrayStr)

	return (world)

def getPath(localMap):
	# Take a map object
	# Return an array of positions
	return [(1,1)]

def sendOutput(infoOut):
	# Write to stdOut
	# Currently assumes printing to terminal
	sys.stdout.write(str(infoOut)+'\n')


def main(): 
    
    # Planned order of operations:
    #   recive info
    #   plan out path
    #   send path back

    infoIn = getInput()
    localMap = worldmap.Map(10)

    path = getPath(localMap)
    
    sendOutput(path)


if __name__ == '__main__':
  main()


# NOTES:
# weighted path algorithm