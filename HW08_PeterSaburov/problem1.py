"""
Peter Saburov
CS 100 2023S Section 012
HW 08, Apr 10, 2023
"""

def initialLetterCount(wordList):
	return_dict = {}
	for word in wordList:
		if word[0] in return_dict:
			return_dict[word[0]] += 1
		else:
			return_dict[word[0]] = 1
	return return_dict

r = initialLetterCount(['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say'])
print(r)

assert initialLetterCount(['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']) == {'I': 4, 's': 2, 'w': 2, 'm': 2, 'a': 1}
assert initialLetterCount([]) == {}
assert initialLetterCount(['wow', 'What', 'a', 'homework', 'test']) == {'w': 1,'W': 1,'a': 1,'h': 1,'t': 1}