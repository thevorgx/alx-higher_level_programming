#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) != 0:
        new_list = set(my_list)
        res = sum(new_list)
        return (res)
    else:
        return ([])
