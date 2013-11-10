import sys

class Cell:
	def __init__( self, direction, score):
		self.direction = direction
		self.score = score
	
	def getScore(self):
		return self.score
	
	def getDirection(self):
		return self.direction

len1 = 5
len2 = 4

myMatrix = [[Cell("init",0) for x in range(0,len2)] for x in range(0,len1)]

for x in range(0, len1):
	for y in range(0,len2):
		print( str(x) + "," + str(y) + ":" +  str( myMatrix[x][y].getScore() ) + " " + str( myMatrix[x][y].getDirection() ) ) 
		

myMatrix[0][1] = Cell("left", -8)
myMatrix[1][0] = Cell("up", -8)

# print it out in a more useful grid
for x in range(0, len1):
	aString = ""
	for y in range(0,len2):
		aString = aString + ( str( myMatrix[x][y].getScore() ) + "_" + str( myMatrix[x][y].getDirection() ) + str("\t") ) 
	print(aString + "\n")
