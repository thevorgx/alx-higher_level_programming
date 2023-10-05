#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    if len(sys.argv) > 1:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in sys.argv[1:]:
            len(sys.argv) == 1
            count += 1
            print("{} : {}".format(count, i))
    else:
        print("{} arguments.".format(len(sys.argv) - 1))
