"""
Peter Saburov
CS 100 2023S Section 012
HW 08, Apr 10, 2023
"""

def shareOneLetter(wordList):
	return_dict = {}
	for word in wordList:
		if not word in return_dict:
			return_dict[word] = []
		for word2 in wordList:
			for letter in word:
				if letter in word2 and not word2 in return_dict[word]:
					return_dict[word].append(word2)
	return return_dict


r = shareOneLetter(['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say'])
print(r)

assert shareOneLetter(['I', 'say', 'what', 'I', 'mean', 'and', 'I', 'mean', 'what', 'I', 'say']) == {'I': ['I'], 'say': ['say', 'what', 'mean', 'and'], 'what': ['say', 'what', 'mean', 'and'], 'mean': ['say', 'what', 'mean', 'and'], 'and': ['say', 'what', 'mean', 'and']}
assert shareOneLetter([]) == {}
assert shareOneLetter(['abc', 'cba', 'def']) == {'abc': ['abc', 'cba'], 'cba': ['abc', 'cba'], 'def': ['def']}