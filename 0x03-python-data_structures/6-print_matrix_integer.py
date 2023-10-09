#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for row in matrix:
            for integer in row:
                print("{}".format(integer), end=' ')
            print()
    else:
        return
