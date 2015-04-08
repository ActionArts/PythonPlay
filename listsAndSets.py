# Print number of unique words in the sentence below
#  "Thrift is poetic because it is creative; waste is unpoetic because it is waste."

import string
none = string.maketrans("", "")

s = "Thrift is poetic because it is creative; waste is unpoetic because it is waste."

# remove the semi-colon and period
s = s.translate(none, ";.")
lst = s.split(" ")

# convert to set of unique words
wordset = set(lst)

for word in wordset:
	print word
