#!/usr/bin/python3
import json
def load_from_json_file(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        j_string = json.load(f)
        return (j_string)
