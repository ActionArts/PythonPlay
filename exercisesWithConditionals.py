# 1: Which line in the list 'y' code causes its output to differ from list 'l' ?

l = [num for num in range(4)]
l.append('four')
l.extend([5.0,6])
l += ['7',16/2,[9,10]]
print 'list l: ', l

y = []
y.extend(range(3))
y.append(['four',5.0])
y += [6,'7',8,[9,10]]
print 'list y: ',y

# 1 answer: if you append a list, it gives you a nested list
#			extend is adding one list to another

# 2a: Print all the numbers under 100 that contain a '4' or a '2'.
val = 100
for num in range(val):
	if ('4' in str(num)) or ('2' in str(num)):
		print num
		
# 2b: Print the sum of all numbers under 100 that contain a '4' or a '2'.
total = 0
for num in range(val):
	if ('4' in str(num)) or ('2' in str(num)):
		total = total + num
print 'sum = ', total

total = sum( num for num in range(val) if ('4' in str(num)) or ('2' in str(num)) )

print 'alternate way of getting sum = ', total

# help(sum)  will give you a definition of the sum function in an interpreter
