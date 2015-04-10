

# Exercise: Print number of unique words in the sentence below
#  "Thrift is poetic because it is creative; waste is unpoetic because it is waste."


originalSentence = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."
print "Original sentence:"
print originalSentence

# maketrans for versions 3+
#noPunctuation = str.maketrans("", "", ";.")
# remove the punctuation for versions 3+
#sentence = originalSentence.translate(noPunctuation)

# maketrans function for versions < 3
import string
none = string.maketrans("", "")
# remove the punctuation: "translate" function for versions < 3
sentence = originalSentence.translate(none, ";.")

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

