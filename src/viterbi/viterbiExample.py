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
		
	def getIndexOfEmission(self, char):
		for i in range(0, len(charsToEmit) ):
			if charsToEmit[i] == char:
				return i
		raise Exception("Cound not find " + char )
				
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

def getMaxIndex( iterable ):
	val = iterable[0]
	index =0
	returnVal =0
	for i in iterable:
		if i < val:
			returnVal = index
		index = index+1
	return returnVal
	

def getViterbiPath( markovStates, output, emissions ):
	viterbiPath = []
	oldViterbiProbs = []
	oldViterbiProbs[0] = 1 # we are 100% sure we start in the first state
	for i in range( 1, len(markovStates) ):
		oldViterbiProbs[i] = 0
	
	for i in range( 0,emissions):
		newViterbiProbs = []
		for j in range( 0, len(markovStates)):
			emissionProb = state.emissionProbs[state.getIndexOfEmission(j)]		
			vTimesA=[]
			for k in range(0, markovStates):
				vTimesA[k] = oldViterbiProbs[j] * markovStates[j].transitionProbs[k]
			maxVal = vTimesA[ getMaxIndex(vTimesA) ]
			newViterbiProbs[j] = emissionProb * maxVal
		viterbiPath[i] = getMaxIndex(newViterbiProbs)	
	return viterbiPath

dice = ( 1,2,3,4,5,6 ) 

fairState = MarkovState( dice, (1/6,1/6,1/6,1/6,1/6,1/6), ( 0.95, 0.05) )
loadedState = MarkovState( dice, (1/10,1/10,1/10,1/10,1/10,5/10), ( 0.10, 0.90) )

states = ( fairState, loadedState ) 

rolls = ""
trueStates = ""
state = states[0]

for i in range( 1, 100):
	nextState = state.getTransitionIndex()
	state = states[ nextState]
	trueStates = trueStates + str(nextState)
	rolls = rolls + str( dice[ state.getEmissionIndex()] )

rolls
trueStates