# Exercise: Print number of unique words in the sentence below
#  "Thrift is poetic because it is creative; waste is unpoetic because it is waste."

sentence = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."


# maketrans for versions 3+
noPunctuation = str.maketrans("", "", ";.")

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
