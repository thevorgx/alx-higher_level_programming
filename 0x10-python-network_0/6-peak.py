#!/usr/bin/python3
"""find peeak number in a list"""


def find_peak(list_of_integers):
    """peak"""
    if not list_of_integers:
        return None

    for i in range(len(list_of_integers)):
        current_element = list_of_integers[i]

        if i == 0:
            continue

        left_value = list_of_integers[i - 1]
        right_value = list_of_integers[i + 1]

        if current_element >= left_value and current_element >= right_value:
            return current_element
