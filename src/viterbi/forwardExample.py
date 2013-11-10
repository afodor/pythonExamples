import random

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


