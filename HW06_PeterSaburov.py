"""
Peter Saburov
CS 100 2023S Section 012
HW 05, Mar 19, 2023
"""


# 1
def twoWords(length, firstLetter):
	while True:
		a = input(f"Enter a {length}-letter word please: ")
		if len(a) == length:
			break
	while True:
		b = input(f"Enter a word beginning with {firstLetter} please: ")
		if b[0].lower() == firstLetter.lower():
			break
	return [a, b]

print(twoWords(4,'b'))


# 2
def twoWordsV2(length, firstLetter):
	a = ''
	while len(a) != length:
		a = input(f"Enter a {length}-letter word please: ")
	b = ' '
	while b[0].lower() != firstLetter.lower():
		b = input(f"Enter a word beginning with {firstLetter} please: ")
	return [a,b]

print(twoWordsV2(4,'b'))


# 3
def enterNewPassword():
	while 1:
		p = input("enter a password: ")
		if len(p) >= 8 and len(p) <= 15:
			for c in p:
				if c in '1234567890':
					return
		print("failed one or both tests")

enterNewPassword()


# 4
from random import randint

def GuessNumber():
	num = randint(0,50)
	guess = int(input("I'm thinking of a number in the range 0-50. You have five tries to guess it\nGuess 1? "))
	for i in range(1,5):
		if guess < num:
			print(f'{guess} is too low')
		elif guess > num:
			print(f'{guess} is too high')
		else:
			print(f"You are right! I was thinking of {num}!")
			return
		guess = int(input(f"Guess {i+1}? "))
	print(f"You are wrong! I was thinking of {num}!")

GuessNumber()
