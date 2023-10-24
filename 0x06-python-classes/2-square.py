#!/usr/bin/python3
"""Define a class named Square to represent a square."""


class Square:
    """
    Constructor method to initialize a Square object.

    Parameters:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
