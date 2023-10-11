#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict0 = (a_dictionary.copy())
    if 'Number' in dict0:
        number = dict0['Number']
        print("Number: {}".format(number))
    else:
        print("{}".format())

    if 'ids' in dict0:
        ids = dict0['ids']
        print("ids: {}".format(ids))
    else:
        print("{}".format())

    if 'language' in dict0:
        language = dict0['language']
        print("language: {}".format(language))
    else:
        print("{}".format())

    if 'track' in dict0:
        track = dict0['track']
        print("track: {}".format(track))
    else:
        print("{}".format())
