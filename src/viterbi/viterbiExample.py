import random

class MarkovState:
	
	def __init__(self,charsToEmit, emissionProbs,transitionProbs):
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

states = ( fairState, loadedState ) 

rolls = ""
trueStates = ""
state = states[0]

for i in range( 1, 1000):
	nextState = state.getTransitionIndex()
	state = states[ nextState]
	trueStates = trueStates + str(nextState)
	rolls = rolls + str( dice[ state.getEmissionIndex()] )

rolls
trueStates