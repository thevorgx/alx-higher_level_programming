#!/usr/bin/python3
for i in range(122, 96, -1):
    print("{0}{1}".format(chr(i - 32 * (i % 2)), chr(i)), end="")

