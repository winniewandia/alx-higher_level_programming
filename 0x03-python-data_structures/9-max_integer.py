#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if not my_list:
        return None
    else:
        max = my_list[0]
        for i in range(1, length - 1):
            if my_list[i] > max:
                max = my_list[i]
        return max
