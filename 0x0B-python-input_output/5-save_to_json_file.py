#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
        j_string = json.dumps(my_obj)
        with open(filename, 'w', encoding='UTF-8') as f:
                return (f.write(j_string))
