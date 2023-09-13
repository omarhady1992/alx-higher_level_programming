#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    ''' A function to an element wise squaring of a matrix '''

    square_matrix = []
    for col in matrix:
        square_list = list(map(lambda x: x**2, col))
        square_matrix.append(square_list)
    return square_matrix
