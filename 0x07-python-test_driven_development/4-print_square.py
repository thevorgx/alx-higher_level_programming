#!/usr/bin/python3
""" print square """


def print_square(size=10):
    """ print square """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            if j != (size - 1):
                print("#", end="")
            else:
                print("#")
