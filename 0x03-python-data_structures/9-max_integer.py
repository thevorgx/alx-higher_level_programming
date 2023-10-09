#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    if my_list is not None:
        for idx in range(len(my_list)):
            if my_list[idx] > max:
                max = my_list[idx]
                idx += 1
        return (max)
    else:
        return (None)
