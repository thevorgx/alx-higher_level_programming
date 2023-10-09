#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 0:
        for row in matrix:
            for number in row:
                print("{:d}".format(number), end=' ')
            print()
    else:
        print("".format())
