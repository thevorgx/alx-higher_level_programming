#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return (res)
    except Exception as error_message:
        return (None)
        print("Exception: {}".format(error_message), file=sys.stderr)
