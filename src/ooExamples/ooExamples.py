


class FastaSequence:
	
	def __init__( self, header, sequence):
		self.header = header
		self.sequence = sequence
		
	def getHeader(self):
		return self.header
		
	def getSequence(self):
		return self.sequence
		

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

	
myGen = fastaAsGen("D:\\classes\\undergradProgramming_2013\\sequences\\NC-016613.faa")

mySeq = next(myGen)

mySeq

mySeq.getHeader()
mySeq.getSequence()

# considered poor form but allowed in Python
mySeq.header
mySeq.sequence








		
	

