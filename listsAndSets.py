

# Exercise: Print number of unique words in the sentence below
#  "Thrift is poetic because it is creative; waste is unpoetic because it is waste."


<<<<<<< HEAD
<<<<<<< HEAD
=======
originalSentence = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."
print "Original sentence:"
print originalSentence
>>>>>>> b7715a4fac4cac9bbed697b1913a4217ea3dc2be

# maketrans for versions 3+
#noPunctuation = str.maketrans("", "", ";.")
# remove the punctuation for versions 3+
#sentence = originalSentence.translate(noPunctuation)

<<<<<<< HEAD
=======
# maketrans for versions 3+
noPunctuation = str.maketrans("", "", ";.")

>>>>>>> 6e6ffaddb5b66ec62210535b75faa2f471346a83
# remove the puncuation
sentence = sentence.translate(noPunctuation)
=======
# maketrans function for versions < 3
import string
none = string.maketrans("", "")
# remove the punctuation: "translate" function for versions < 3
sentence = originalSentence.translate(none, ";.")
>>>>>>> b7715a4fac4cac9bbed697b1913a4217ea3dc2be

# could also have done: sentence = sentence.replace(";").replace(".")

#lowercase it
sentence = sentence.lower()

# split to a list - no arguments will split on whitespace
wordlist = sentence.split()

# convert to set of unique words
wordset = set(wordlist)

print "Sentence reduced to original lowercase words only:"
for word in wordset:
	print (word)

<<<<<<< HEAD
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
=======
#join the set into comma-separated string
csWordset = ",".join(wordset)

#Lets rebuild the sentence!
# insert the punctuation back to where it was
semiColonIndex = originalSentence.index(";");
periodIndex = originalSentence.index(".");
characterList = list(sentence)
characterList.insert(semiColonIndex,";")
characterList.insert(periodIndex+1,".")

#This will join and put in a space character - weird
newSentence = "".join(characterList)

#capitalize it
newSentence = newSentence.capitalize()

print "Rebuilt sentence:"
print newSentence

	
# e = f    #e is a reference to f
# e = f[:] #this makes a copy of f into a new object, e

>>>>>>> b7715a4fac4cac9bbed697b1913a4217ea3dc2be
