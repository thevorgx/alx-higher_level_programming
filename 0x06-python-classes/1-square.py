#!/usr/bin/python3
"""Define a class named Square to represent a square."""


class Square:
    """
    Constructor method to initialize a Square object.

    Parameters:
        size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initialize a new Square with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size__ = size
