#!/usr/bin/python3
"""inherits from"""


def inherits_from(obj, a_class):
    """inherits from"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)
