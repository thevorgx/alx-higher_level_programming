#!/usr/bin/python3
"""Define a class named Rectangle to represent a rectangle."""


class Rectangle:
    """Constructor method to initialize a Rectangle object."""
    def __init__(self, width=0, hight=0):
        """Initialize a new Rectangle with the given width."""
        self.__width = width
        self.__hight = hight

    @property
    def width(self):
        """property width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """property setter width"""
        self.__width = value
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def hight(self):
        """property hight"""
        return (self.__hight)

    @hight.setter
    def hight(self, value):
        """property setter width"""
        self.__width = value
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
