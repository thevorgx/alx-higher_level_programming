#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    new_list = set(my_list)
    for number in new_list:
        res += number
    return (res)
