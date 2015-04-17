#Open a CSV file on your computer, read it in, processes it, and print it out in a way that's nice to read. 
#Assume that no record (aka, row) ever exceeds four columns, but that it can have missing fields.

# Requirements:

# You should try to justify the text consistently like the sample output below
# Also, try to be as fault-tolerant as possible. If a field is missing, do you handle that? What if age data ends up in the profession column?
# sample printcsv.py output

# firstName  |  lastName  |  age  |  profession

# Michael       Jordan       52      Basketball Player
# Kirsten       Bell         39      Actress
# Morrissey                  60      Musician  


f = open('test_csv.txt','r')
lines = f.readlines()
f.close()

parsedCsv = ""
pad = " "
longestValueInLine = 1

#loop through each line, split on the comma, and store (the length of the longest string) for each column
for line in lines:
	values = line.split(',')
	for value in values:
		if value != "" and len(value) > longestValueInLine:
			longestValueInLine = len(value)

#loop through each line again, split on the comma, and print string + spaces for (longest string - string.len()
for index, ln in enumerate(lines):
	formattedLine = ""
	delim = " "
	if index == 0:
		delim = "|"

	vals = ln.split(',')
	for i, val in enumerate(vals):
		if(i == len(vals) - 1):
			formattedLine = "{}{}{}".format(formattedLine, pad, val)
		elif val == "":
			offsetSpaces = " " * longestValueInLine
			formattedLine = "{}{}{}{}{}{}".format(formattedLine, pad, val, offsetSpaces, pad, delim)
		else:
			offsetValue = longestValueInLine - len(val)
			offsetSpaces = " " * offsetValue
			formattedLine = "{}{}{}{}{}{}".format(formattedLine, pad, val, offsetSpaces, pad, delim)
	print formattedLine
