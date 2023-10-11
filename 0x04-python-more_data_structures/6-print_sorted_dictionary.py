#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict0 = a_dictionary.copy()
    number = dict0.get('Number')
    ids = dict0.get('ids')
    language = dict0.get('language')
    track = dict0.get('track')
    print("Number: {}".format(number))
    print("ids: {}".format(ids))
    print("language: {}".format(language))
    print("track: {}".format(track))
