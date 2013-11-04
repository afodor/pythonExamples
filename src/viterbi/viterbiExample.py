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

def getMaxIndex( iterable ):
	val = iterable[0]
	index =0
	returnVal =0
	for i in iterable:
		if i > val:
			returnVal = index
		index = index+1
	return returnVal

def getViterbiPath( markovStates, output):
	returnPath= []
	oldViterbiProbs = []
	oldViterbiProbs.append(1) # we are 100% sure we start in the first state
	for i in range( 1, len(markovStates) ):
		oldViterbiProbs.append( 0)
	aTuple = ( oldViterbiProbs, 0)
	returnPath.append( aTuple )
	
	for i in range( 0,len(output)):
		newViterbiProbs = []
		for j in range( 0, len(markovStates)):
			state = markovStates[j]
			emissionProb = state.emissionProbs[state.getIndexOfEmission(output[i])]		
			vTimesA=[]
			for k in range(0, len(markovStates)):
				vTimesA.append (oldViterbiProbs[k] * markovStates[k].transitionProbs[j])
			#print( "vTimesA" + str( vTimesA))
			maxVal = vTimesA[ getMaxIndex(vTimesA) ]
			newViterbiProbs.append( emissionProb * maxVal)
		aTuple = (newViterbiProbs,getMaxIndex(newViterbiProbs))
		returnPath.append( aTuple)
		oldViterbiProbs = newViterbiProbs
	return returnPath

dice = ( 1,2,3,4,5,6 ) 

fairState = MarkovState( dice, (1/6,1/6,1/6,1/6,1/6,1/6), ( 0.95, 0.05) )
loadedState = MarkovState( dice, (1/10,1/10,1/10,1/10,1/10,5/10), ( 0.10, 0.90) )

states = ( fairState, loadedState ) 

################################################

rolls = "266666"
getViterbiPath( states, rolls)

################################################
rolls = ""
trueStates = ""
state = states[0]

for i in range( 1, 50):
	nextState = state.getTransitionIndex()
	state = states[ nextState]
	trueStates = trueStates + str(nextState)
	rolls = rolls + str( dice[ state.getEmissionIndex()] )

rolls
trueStates

viterbiPath = getViterbiPath( states, rolls)

for i in range(0, len(rolls)):
	print( str(rolls[i]) + " " + str(trueStates[i])+ " " + str(viterbiPath[i][1]))

################################################

