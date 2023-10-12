#!/usr/bin/python3
def best_score(a_dictionary):
    maxvalue = 0
    best_key = 0
    if a_dictionary is not None:
        for key, value in a_dictionary.items():
            if maxvalue is None or value > maxvalue:
                maxvalue = value
                best_key = key
        return (best_key)
    else:
        return (None)
