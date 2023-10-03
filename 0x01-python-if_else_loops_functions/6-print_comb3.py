#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1+i, 10):
        print("{}{}".format(i, j), end=', ' if not (i == 8) else '\n')
