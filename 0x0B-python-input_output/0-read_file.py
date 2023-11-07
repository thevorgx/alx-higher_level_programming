#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.read()
    print(lines)
