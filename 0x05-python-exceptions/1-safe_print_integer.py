#!/usr/bin/python3
def safe_print_integer(value):
    if value:
        try:
            print("{:d}".format(value), end="\n")
            return (True)
        except ValueError:
            return (False)
