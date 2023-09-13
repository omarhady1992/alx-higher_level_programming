#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    '''Prints dictionary keys sorted alphabetically'''

    keys = [a_dictionary.keys()]
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
