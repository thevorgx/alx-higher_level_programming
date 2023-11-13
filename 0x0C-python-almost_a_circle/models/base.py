#!/usr/bin/python3
"""Class Base"""


import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor __init__"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Dictionary to JSON string"""
        if list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a file in JSON format"""
        fname = f"{cls.__name__}.json"
        if list_objs is None:
            list_objs = []
        dlist = []
        for idx in list_objs:
            dlist.append(idx.to_dictionary())
        with open(fname, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(dlist))

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary"""
        m_list = []
        if json_string is None or len(json_string) == 0:
            return (m_list)
        else:
            return (json.loads(json_string))
