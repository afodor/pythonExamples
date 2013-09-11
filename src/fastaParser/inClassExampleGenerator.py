#this code has not been tested..


# returns a tuple with sequences and quals scores 
def getQualScoreLines(filepath):
	f = open(filepath)
	seq = ""
	i = 0
	for line in f:
		if( i % 4 == 1 ):
			seq = line.rstrip() 
		if( i % 4 == 3):
			yield ( seq,  line.rstrip()) 
			seq =""
		i = i + 1
	f.close()
	
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


writeStatsFile("C:\\classes\\undergradProgramming_2013\\sequences\\example.fastq", "C:\\classes\\undergradProgramming_2013\\sequences\\fileOut.txt")
myGen = getQualScoreLines("C:\\classes\\undergradProgramming_2013\\sequences\\example.fastq")
