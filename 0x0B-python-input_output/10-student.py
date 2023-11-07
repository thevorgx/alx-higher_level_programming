#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json method"""
        if not isinstance(self, object):
            return None
        return (vars(self))
