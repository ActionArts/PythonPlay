# Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” 
# instead of the number and for the multiples of five print “Buzz”. For numbers which are 
# multiples of both three and five print “FizzBuzz”. 

counter = 1

while counter < 101:
	if counter % 3 == 0 and counter % 5 == 0:
		print 'fizzbuzz'
	elif counter % 3 == 0:
		print 'fizz'
	elif counter % 5 == 0:
		print 'buzz'
	else:
		print counter

	counter = counter  + 1