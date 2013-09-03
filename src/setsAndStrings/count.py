


def count_chars(s):
    countMap = {}
    
    for c in s:
    	countMap.setdefault(c, 0)
    	countMap[c] += 1	
	
	return countMap
