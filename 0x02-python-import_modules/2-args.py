#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv) - 1
    if length == 0:
        print("{} arguments".format(0))
    elif length == 1:
        print("{} argument".format(1))
        print("{}: {}".format(1, argv[1]))
    else:
        print("{} arguments".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, argv[i]))
