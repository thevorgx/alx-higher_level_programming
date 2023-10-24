#!/usr/bin/python3
"""Define a class named Square to represent a square."""


class Square:
    """Constructor method to initialize a Square object."""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        area = self.__size ** 2
        return (area)

    @property
    def size(self):
        """property"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """property setter"""
        self.__size = value
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
