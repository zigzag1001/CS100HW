"""
Peter Saburov
CS 100 2023S Section 012
HW 10, Apr 21, 2023
"""

class Dog():
	'''dog'''

	species = 'Canis familiaris'

	def __init__(self, name, breed):
		self.name = name
		self.breed = breed
		self.tricks = list()

	def teach(self, trick):
		self.tricks.append(trick)
		print(self.name, 'knows', trick)

	def knows(self, trick):
		r = trick in self.tricks
		print(f'Yes, {self.name} knows {trick}') if r else print(f'No, {self.name} dosen\'t know {trick}')
		return r