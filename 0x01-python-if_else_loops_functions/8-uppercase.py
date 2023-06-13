#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            value = 32
        else:
            value = 0
        print("{:c}".format(ord(str[i]) - value), end='')
    print()


uppercase("none")
uppercase("Best School 98 Battery street")
