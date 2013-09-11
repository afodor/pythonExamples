


def getDoublingNumbers():
	x = 1
	while x <= 128:
		yield x
		x = x * 2
		
myGen = getDoublingNumbers()

aVal = next(myGen)

while( aVal != None):
	aVal = next(myGen,None)
	print( aVal ) 