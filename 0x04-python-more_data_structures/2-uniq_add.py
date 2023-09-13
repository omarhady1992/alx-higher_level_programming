#!/usr/bin/python3


def add_uniq(my_list=[]):
    ''' Adds unique integers of a list'''

    list_a = []
    sums = 0
    for i in my_list:
        if i not in list_a:
            sums += i
            list_a.append(i)
    return sums
