
def fastaAsGenerator(filepath):
	f = open(filepath)
	header = f.readline()
	while( len(header) > 0 ):
		seq = ""
		aLine = f.readline()
		while len(aLine) >0 and not aLine.startswith(">"):
			seq = seq + aLine
			aLine = f.readline()
		yield ( header.replace("\n",""), seq.replace("\n","" ) ) 
		header = aLine		
	f.close()
	
def gcContent(fastaSeq):
	return fastaSeq.count("C") + fastaSeq.count("G")

myGen = fastaAsGenerator("C:\\classes\\undergradProgramming_2013\\sequences\\test.fasta")

aList = []

for seq in myGen:
	aList.append(seq)

sorted( aList, key=gcContent) 

sorted(myGen)

next(myGen)