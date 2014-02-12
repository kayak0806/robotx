'''
	Importaint:
	Main must take a stdin input
	In terminal:
	echo _input_ | pyhton main.py
	OR
	cat input.txt | python main.py
'''

# Main run file
import math
import fileinput
import sys
import items
import worldmap

def parseStr(arrayStr):
	return eval(arrayStr)

def getInput():
	# read from stdin
	# Assume the input is a list of lists representing the world
	arrayStr = ""
	for line in fileinput.input():
		line=line.rstrip()
		arrayStr += line
	return parseStr(arrayStr)

def getPath(localMap):
	return [(1,1)]

def sendOutput(path):
	# write to stdOut
	# Currently assumes printing to terminal
	sys.stdout.write(str(path)+'\n')


def main(): 
    
    # Planned order of operations:
    #   recive info
    #   plan out path
    #   send path back

    mapIn = getInput()
    # localMap = worldmap.Map()
    path = getPath(mapIn)
    sendOutput(path)




if __name__ == '__main__':
  main()


# NOTES:
# weighted path algorithm