"""
Peter Saburov
CS 100 2022S Section 012
HW 02, Febuary 01, 2023
"""


# 1

a, b, c = 3, 4, 5

if a < b:
	print("OK")

if c < b:
	print("OK")

if a + b == c:
	print("OK")

if a**2 + b**2 == c**2:
	print("OK")


# 2

if a < b:
	print("OK")
else:
	print("NOT OK")

if c < b:
	print("OK")
else:
	print("NOT OK")

if a + b == c:
	print("OK")
else:
	print("NOT OK")

if a**2 + b**2 == c**2:
	print("OK")
else:
	print("NOT OK")


# 3

grades = ['A', 'B', 'C', 'D', 'F', 'C', 'B', 'C', 'A', 'D']

frequency = [grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('F')]

# 4

dog_breeds = ['collie', 'sheepdog', 'Chow', 'Chihuahua']

herding_dogs = dog_breeds[:2]

tiny_dogs = [dog_breeds[-1]]

if 'Persian' in dog_breeds:
	print(True)
else:
	print(False)