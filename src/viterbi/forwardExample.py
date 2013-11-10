import random

import math
from math import isinf

def logPAddedToQ( logP, logQ ):
	if( isinf( logP ) and logP < 0):
		return logQ
		
	return logP + math.log( 1 + math.exp( logQ - logP))

class MarkovState:
	
	def __init__(self,charsToEmit, emissionProbs,transitionProbs):
		self.charsToEmit = charsToEmit
		self.emissionProbs = emissionProbs
		self.transitionProbs = transitionProbs
		
	def getEmissionIndex(self):
		aRand = random.random()
		cumulative = 0
		index =0
		for val in self.emissionProbs:
			cumulative += val
			if aRand <= cumulative:
				return index
			index = index + 1
		return len(self.emissionProbs) - 1
		
	def getIndexOfEmission(self, char):
		for i in range(0, len(self.charsToEmit) ):
			if str(self.charsToEmit[i]) == str(char):
				return i
		raise Exception("Cound not find " + str(char) )
				
	def getTransitionIndex(self):
		aRand = random.random()
		cumulative = 0
		index =0
		for val in self.transitionProbs:
			cumulative += val
			if aRand <= cumulative:
				return index
			index = index + 1
		return len(self.transitionProbs) - 1

dice = ( 1,2,3,4,5,6 ) 

#######################
#
# run the forward algorithm in unlogged space
#
######################

fairState = MarkovState( dice, (1/6,1/6,1/6,1/6,1/6,1/6), ( 0.95, 0.05) )
loadedState = MarkovState( dice, (1/10,1/10,1/10,1/10,1/10,5/10), ( 0.10, 0.90) )

states = (fairState, loadedState)

rolls = "326"

oldProbs = []
oldProbs.append(0.7)
oldProbs.append(0.3)

print(oldProbs)
for num in rolls:
	newProbs = []
	for i in range(0,len(states)):
		prob =0
		for j in range(0,len(states)):
			prob = prob + oldProbs[j] * states[j].transitionProbs[i]
		prob = prob * states[i].emissionProbs[ states[i].getIndexOfEmission(num)]
		newProbs.append(prob)
	oldProbs = newProbs
	print(newProbs)

px = 0.0001 * newProbs[0] + 0.0001 * newProbs[1]
px

##############################################
# 
#  test the adding log space
#
############################################

p = 0.0001
q = 0.000001

math.log(p+q)

logP = math.log(p)
logQ = math.log(q)

logPAddedToQ( logP, logQ)

##################################################
#
#  The forward algorithm in log space 
#
#################################################

def printExpVals( iterable ):
	s = ""
	for i in iterable:
		s = s + str(math.exp(i)) + "\t"
	print (s)

fairState = MarkovState( dice, (1/6,1/6,1/6,1/6,1/6,1/6), ( 0.95, 0.05) )
loadedState = MarkovState( dice, (1/10,1/10,1/10,1/10,1/10,5/10), ( 0.10, 0.90) )

states = (fairState, loadedState)

rolls = "326"

oldProbs = []
oldProbs.append( math.log( 0.7))
oldProbs.append(math.log(0.3))
printExpVals(oldProbs)

for num in rolls:
	newProbs = []
	for i in range(0,len(states)):
		prob = float("-inf")
		for j in range(0,len(states)):
			prob = logPAddedToQ(  prob , oldProbs[j] + math.log( states[j].transitionProbs[i]))
		prob = prob + math.log( states[i].emissionProbs[ states[i].getIndexOfEmission(num)])
		newProbs.append(prob)
	oldProbs = newProbs
	printExpVals(newProbs)

px = logPAddedToQ( math.log( 0.0001)  + newProbs[0] , math.log( 0.0001) + newProbs[1])
px
math.exp(px)
