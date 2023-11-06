#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """BaseGeometry"""

    def area(self):
        """area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validation"""
        if not type(value) is int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
