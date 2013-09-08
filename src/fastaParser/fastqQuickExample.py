
def f1(filepath):
	f = open(filepath)
	strings= f.read()
	f.close()
	return strings.split("\n")

def f2(filepath):
	strings = f1(filepath)
	myList = []
	index =0
	while( index < len(strings )):
		myTuple = tuple( strings[index:index+4])
		myList.append( myTuple )
		index += 4
	return myList[0:len(myList)-1] 

def numOverThreshold(filepath,threshold):
	numOver =0
	myList = f2(filepath)
	for tup in myList:
		sum =0
		for i in tup[3]:
			sum += ord(i) - 64	
		if sum / len(tup[3]) > threshold:
			numOver += 1
	return numOver
	
f1("D:\\classes\\undergradProgramming_2013\\sequences\\shortFastq.txt")
	
f2("D:\\classes\\undergradProgramming_2013\\sequences\\shortFastq.txt")

print(numOverThreshold("D:\\classes\\undergradProgramming_2013\\sequences\\shortFastq.txt",20))

print(numOverThreshold("D:\\classes\\undergradProgramming_2013\\sequences\\example.fastq",20))


