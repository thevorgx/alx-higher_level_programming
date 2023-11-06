#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validation"""
        self.name = name
        self.value = value
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


"""Rectangle child class"""


class Rectangle(BaseGeometry):
    """Rectangle child class"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        self.integer_validator("width", height)

    def area(self):
        """area implemented"""
        res = self.__width * self.__height
        return (res)

    def __str__(self):
        """str"""
        return (f"[Rectangle] {self.__width}/{self.__height}")
