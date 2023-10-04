#!/usr/bin/python3
def fizzbuzz():
    str1 = "FizzBuzz"
    str2 = "Fizz"
    str3 = "Buzz"
    space = " "
    for i in range(1, 101):
        if i % 15 == 0:
            print("{}".format(str1), end='')
        elif i % 3 == 0:
            print("{}".format(str2), end='')
        elif i % 5 == 0:
            print("{}".format(str3), end='')
        else:
            print("{}".format(i), end='')
        if i != 101:
            print("{}".format(space), end='')
