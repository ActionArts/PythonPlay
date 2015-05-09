# a program that doubles the square of
# a third of the reverse of the str()
# of the max of this list: [01,94,30,3.0,53]

import random
import math


def gen_sample_space():
    """
    a list of strings to choose from when generating a pseudo-random string
    """
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def gen_random_string(n, sspace):
    """
    gen_random_string(n,sspace) -> pseudo-random string of length n, using chars from sample space.
    """
    if n < 1:
        return ''
    resulting_string = ''
    while n:
        resulting_string = resulting_string + random.choice(sspace)
        n = n - 1
    return resulting_string


def get_max_of_list(the_list):
    return max(the_list)


def one_third_of_reverse_string_of_num(num):
    reversed_num = (str(num))[::-1]
    return float(reversed_num) / 3


def double_the_square(num):
    return math.sqrt(num) * 2


def main():
    sample_space = gen_sample_space()
    print "The example \"Random String\" function results:"
    print gen_random_string(0, sample_space)

    print "Results of program - doubles the square of a third of the reverse of the str() of the max of this list: [01,94,30,3.0,53]"

    result = double_the_square(one_third_of_reverse_string_of_num(get_max_of_list([01, 94, 30, 3.0, 53])))
    print result


main()