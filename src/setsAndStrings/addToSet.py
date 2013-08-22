# time code from http://stackoverflow.com/questions/6999726/python-getting-millis-since-epoch-from-datetime

import datetime


def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return unix_time(dt) * 1000.0


def addToSet(num):
	mySet = set()

	for i in range(num):
		mySet.add("A" + str(i))

def addToList(num):
	mySeq = ""

	for i in range(num):
		mySeq = mySeq + str(i) 


num=3000000

startTime = unix_time_millis( datetime.datetime.now())
addToSet(num)
endTime = unix_time_millis( datetime.datetime.now())

print( (endTime - startTime) / 1000 ) 


startTime = unix_time_millis( datetime.datetime.now())
addToList(num)
endTime = unix_time_millis( datetime.datetime.now())
print( (endTime - startTime) / 1000 ) 
