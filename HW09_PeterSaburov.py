"""
Peter Saburov
CS 100 2023S Section 012
HW 09, Apr 14, 2023
"""

def safeOpen(filename):
	try:
		with open(filename, 'r') as f:
			return f
	except FileNotFoundError:
		return None

print(safeOpen('notHere.bat'))


def safeFloat(x):
	try:
		return float(x)
	except ValueError:
		return 0.0

print(safeFloat('abc'))


def averageSpeed():
	avgSpeedList = []
	for i in range(2):
		fileName = input('Enter file name: ')
		fileObj = safeOpen(fileName)
		if fileObj != None:
			break
		elif i == 1:
			print('File not found. Yet another human error. Goodbye.')
			return
		print('File not found. Please try again.')
	with open(fileName, 'r') as f:
		fileTxtLines = f.readlines()
	for line in fileTxtLines:
		if line.count(' ') > 0:
			badline = line.split()
			for val in badline:
				if safeFloat(val) >= 2:
					avgSpeedList.append(safeFloat(val))
		elif safeFloat(line) >= 2:
				avgSpeedList.append(safeFloat(line))
	print(f'Average speed is {round(sum(avgSpeedList)/len(avgSpeedList), 2)} miles per hour.')

averageSpeed()