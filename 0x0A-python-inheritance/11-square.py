#!/usr/bin/python3
"""import Square classe"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square child class"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area implemented"""
        return (self.__size ** 2)

    def __str__(self):
        """str"""
        return (f"[Rectangle] {self.__size}/{self.__size}")
