# Exercise: Print number of unique words in the sentence below
#  "Thrift is poetic because it is creative; waste is unpoetic because it is waste."

sentence = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."

<<<<<<< HEAD

# maketrans for versions 3+
noPunctuation = str.maketrans("", "", ";.")

=======
# maketrans for versions 3+
noPunctuation = str.maketrans("", "", ";.")

>>>>>>> 6e6ffaddb5b66ec62210535b75faa2f471346a83
# remove the puncuation
sentence = sentence.translate(noPunctuation)

# # maketrans function for versions < 3
# import string
# none = string.maketrans("", "")

# # remove the punctuation: "translate" function for versions < 3
# sentence = sentence.translate(none, ";.")

# split to a list on the space character
wordlist = sentence.split(" ")

# convert to set of unique words
wordset = set(wordlist)

for word in wordset:
	print (word)

#list assignment
a = [1,2,3]
c = a       # c is an alias for a, so c[0] is really a[0]
a[0] = 3    # a is [3,2,3]
c[0] = 1    # a is back to the old [1,2,3]
print a, ' ** ', c  #prints '[1,2,3] ** [1,2,3]'

a = [1,2,3]
c = a[:]  	# a is copied into c, and thus c is independent from a
a[0] = 8
c[0] = 5
print a, ' ** ', c  #prints '[8,2,3] ** [5,2,3]'

# if you know the number of items in a list, you can name each assign a name to each item by separating the names by commas
a=[1,2,3]
one, two, three = a[:]
print "printing a..."
print a
print "printing one,two,three..."
print one,two,three
