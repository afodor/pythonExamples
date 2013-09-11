#this code has not been tested..


# returns a tuple with sequences and quals scores 
def getQualScoreLines(filepath):
	f = open(filepath)
	mySeqs = []
	myQualScoreLines = []	
	i = 0
	for line in f:
		if( i % 4 == 1 ):
			mySeqs.append(line.rstrip()) 
		if( i % 4 == 3):
			myQualScoreLines.append(line.rstrip())
		i = i + 1
	f.close()
	returnList = []
	for j in range(0,len(mySeqs)-1):
		returnList.append( ( mySeqs[j], myQualScoreLines[j] ) ) 
	return returnList

# given a qualscore string, return average qual score
# casting to integer and subtracting 64
def getAverageQualScore( qualScoreLine ):
	sum = 0
	for c in qualScoreLine:
		sum += ord(c) - 64
	return sum / len(qualScoreLine)

def getGCFraction( qualScoreLine ):
	sum =0
	for c in qualScoreLine:
		if( c == 'G' or c == 'C' ):
			sum += 1
	return sum / len(qualScoreLine ) 

def writeStatsFile( inFile, outFile ):
	myList = getQualScoreLines(inFile)
	f = open(outFile, "w")
	f.write("averageQualScore\tgcFraction\n")	
	for line in myList:
		f.write(str(getAverageQualScore(line[1]))+"\t"+str(getGCFraction(line[0]))+"\n")
	f.close()



writeStatsFile("C:\\af\\example.fastq", "c:\\af\\sequenceStats.txt")

getQualScoreLines("C:\\af\\example.fastq")
