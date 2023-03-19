"""
Peter Saburov
CS 100 2023S Section 012
HW 04, Mar 03, 2023
"""

# 1

# a
def hasFinalLetter(strList, letters):
	r = []
	for s in strList:
		if s[-1] in letters:
			r.append(s)
	return r
	# return [s for s in strList if s[-1] in letters]

# b
test_strList1 = ['apple','orange','banana','bean']

test_let1 = 'amklop'

print(hasFinalLetter(test_strList1, test_let1),"should be",['banana'])

test_strList2 = ['abcde','create','loan','edcba']

test_let2 = 'iouplkjmbvc'

print(hasFinalLetter(test_strList2, test_let2),"should be",[])

test_strList3 = ['cha','mean','programme','youtube']

test_let3 = 'aeioun'

print(hasFinalLetter(test_strList3, test_let3),"should be",['cha','mean','programme','youtube'])


# 2

# a
def isDivisible(maxInt, twoInts):
	r = []
	for i in range(1, maxInt):
		if i % twoInts[0] == 0 and i % twoInts[1] == 0:
			r.append(i)
	return r


# b
test_max1 = 11

test_twoInts1 = (2, 5)

print(isDivisible(test_max1, test_twoInts1),"should be",[10])

test_max2 = 21

test_twoInts2 = (1, 10)

print(isDivisible(test_max2, test_twoInts2),"should be",[10, 20])

test_max3 = 10

test_twoInts3 = (3, 7)

print(isDivisible(test_max3, test_twoInts3),"should be",[])






# Actual test cases

# Test cases final letter
test_strList1 = ['apple','orange','banana','bean']

test_let1 = 'amklop'

assert hasFinalLetter(test_strList1, test_let1) == ['banana']

test_strList2 = ['abcde','create','loan','edcba']

test_let2 = 'iouplkjmbvc'

assert hasFinalLetter(test_strList2, test_let2) == []

test_strList3 = ['cha','mean','programme','youtube']

test_let3 = 'aeioun'

assert hasFinalLetter(test_strList3, test_let3) == ['cha','mean','programme','youtube']


# Test cases divisible
test_max1 = 11

test_twoInts1 = (2, 5)

assert isDivisible(test_max1, test_twoInts1) == [10]

test_max2 = 21

test_twoInts2 = (1, 10)

assert isDivisible(test_max2, test_twoInts2) == [10, 20]

test_max3 = 10

test_twoInts3 = (3, 7)

assert isDivisible(test_max3, test_twoInts3) == []