#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix[0]) != 0:
        res = [[idx ** 2 for idx in row] for row in matrix]
        return (res)
