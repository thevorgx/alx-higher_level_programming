#!/usr/bin/python3
def uppercase(str):
    uppc = ""
    for i in str:
        if ord(i) <= 122 and ord(i) >= 97:
            uppc = chr(ord(i) - 32)
        else:
            uppc = i
        print("{}".format(uppc), end='')
    print("")
