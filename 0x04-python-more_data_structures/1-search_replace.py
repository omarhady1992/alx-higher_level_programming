#!/usr/bin/python3


def search_replace(my_list, search, replace):
    ''' A function that replaces
    occurences of an element of a list by another '''

    for i in range(0, len(my_list)):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list
