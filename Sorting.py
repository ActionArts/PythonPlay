"""Given this list of words below,
write the code to print out the same list in descending order,
sorted according to the number of occurrences of the letter 'e' in each word.
Also, give the 'e count' on the same line, separated by a single white-space.

Your output should look like this:

representative 4
ex-developer 4
bespectacled 3
senile 2
effluent 2
elegiac 2
numeric 1
ear 1
"""

words = ['representative', 'numeric', 'senile', 'effluent',
         'ear', 'bespectacled', 'elegiac', 'ex-developer']


def count_char(word):
    num = word.count('e')
    return num


def sort_list():
    sorted_words = sorted(words, key=count_char, reverse=True)
    for w in sorted_words:
        print w, count_char(w)
    pass

sort_list()