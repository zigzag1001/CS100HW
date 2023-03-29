"""
Peter Saburov
CS 100 2023S Section 012
HW 07, Mar 19, 2023
"""

# 1
def file_copy(in_file, out_file):
	with open(in_file, 'r') as inf:
		with open(out_file, 'w') as outf:
			print('\ncreated', out_file, '\n')
			outf.write(inf.read())

file_copy("HW07_PeterSaburov.py", "copiedFile.py")


# 2
def file_stats(in_file):
	with open(in_file, 'r') as inf:
		inf_text = inf.read()
	lines = len(inf_text.split('\n'))
	words = len(inf_text.split())
	chars = len(inf_text)
	print(f"lines {lines}\nwords {words}\ncharacters {chars}\n")

file_stats("copiedFile.py")


# 3
import string

def repeat_words(in_file, out_file):
	with open(in_file, 'r') as inf:
		inf_text = inf.read()
	lines = inf_text.split('\n')
	with open(out_file, 'w') as outf:
		print('created', out_file, '\n')
		for line in lines:
			words = line.split()
			rep_words = []
			for word in words:
				words[words.index(word)] = word.strip().strip(string.punctuation).lower()
			for word in words:
				if words.count(word) > 1 and not word in rep_words:
					outf.write(word + ' ')
					rep_words.append(word)
			outf.write('\n')

repeat_words('catInTheHat.txt','catRepWords.txt')