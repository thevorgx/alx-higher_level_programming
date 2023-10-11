#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    res = []
    if len(matrix) != 0:
        res = [[idx ** 2 for idx in row] for row in matrix]
        return (res)
    else:
        return
