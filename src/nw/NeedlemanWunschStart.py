
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