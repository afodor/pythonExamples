


class FastaSequence:
	
	def __init__( self, header, sequence):
		self.header = header
		self.sequence = sequence
		
	def getHeader(self):
		return self.header
		
	def getSequence(self):
		return self.sequence
	
	def getGCContent(self):
		return (self.sequence.count("C") + self.sequence.count("G")) / float(len(self.sequence))		

#returns a tuple with (header,sequence) 
def fastaAsGen(filepath):
	f=open(filepath)
	header=f.readline()
	line=f.readline()
	seq=""
	while( len(line) > 0 ):
		seq = seq + line
		line = f.readline()
		if line.startswith(">") or len(line)==0:
			yield ( FastaSequence( header.replace("\n",""), seq.replace("\n","")) )
			header = line
			seq = ""
			line = f.readline() 
	f.close()		

	
myGen = fastaAsGen("D:\\classes\\undergradProgramming_2013\\sequences\\NC-005363.ffn")

mySeq = next(myGen)

mySeq

mySeq.getHeader()
mySeq.getSequence()
mySeq.getGCContent()

# considered poor form but allowed in Python
mySeq.header
mySeq.sequence

myGen = fastaAsGen("D:\\classes\\undergradProgramming_2013\\sequences\\NC-005363.ffn")
f = open("c:\\temp\\gcContent.txt", "w")

for fastaSeq in myGen:
	f.write( str(fastaSeq.getGCContent()) + "\n")
	
f.close()








		
	

