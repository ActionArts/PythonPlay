#Sum all the numbers containing a '9' between 0-50 and 100-150, non-inclusive (meaning, the upper bound of each range is not included)

totalsum = 0

counter = 0

while counter < 150:
	if counter < 50 or counter > 99:
		if '9' in str(counter):
			totalsum = totalsum + counter

	counter = counter  + 1

print "total sum = ", totalsum