#!/usr/bin/python3
"""Define a class named Rectangle to represent a rectangle."""


class Rectangle:
    """Constructor method to initialize a Rectangle object."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle width the given width."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
    def height(self):
        """property height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """property setter height"""
        self.__height = value
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Calculate and return the area of the rectangle."""
        area = self.width * self.height
        return (area)

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.height == 0 or self.width == 0:
            perimeter = 0
        else:
            perimeter = self.width * 2 + self.height * 2
        return (perimeter)

    def __str__(self):
        rectangle_str = ""
        if self.height == 0 or self.width == 0:
            return ("")
        for idx in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + "\n"
        return (rectangle_str.rstrip("\n"))

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not type(rect_1) is Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
