
# a slow n^2 naive sorting algorithm
def bubbleSort( aList ):
	for i in range(0 , len(aList) -1 ):
		for j in range( i + 1 , len(aList ) ):
			if( aList[i] > aList[j] ):
				temp = aList[i]
				aList[i] = aList[j]
				aList[j] = temp

myList = [1,2,31,2,1,2,3,4,5,0,-1,3,4]
myList
bubbleSort(myList)
myList

myList = ["A", "C", "Z", "E", "Y", "Roger"]
myList
bubbleSort(myList)
myList
				