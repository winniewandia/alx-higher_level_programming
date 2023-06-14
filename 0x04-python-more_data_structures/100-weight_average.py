#!/usr/bin/python3
def weight_average(my_list=[]):
    i = 0
    j = 0
    if not my_list:
        return 0
    for k in my_list:
        i += k[0] * k[1]
        j += k[1]

    return i / j
