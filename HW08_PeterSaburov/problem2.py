"""
Peter Saburov
CS 100 2023S Section 012
HW 08, Apr 10, 2023
"""

def initialLetters(wordList):
	return_dict = {}
	for word in wordList:
		if word[0] in return_dict:
			if not word in return_dict[word[0]]:
				return_dict[word[0]].append(word)
		else:
			return_dict[word[0]] = [word]
	return return_dict

r = initialLetters(['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say'])
print(r)

assert initialLetters(['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']) == {'I': ['I'], 's': ['say'], 'w': ['what'], 'm': ['mean'], 'a': ['and']}
assert initialLetters([]) == {}
assert initialLetters(['whats','with','wings','that','wing']) == {'w': ['whats','with','wings','wing'], 't': ['that']}